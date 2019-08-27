"""Class for managing back-end server operations"""
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import os
import signal
import sys
import time
import threading
import asyncio
import cursesmenu
import tornado.ioloop
import tornado.web

from DatabaseManager import DatabaseManager, DatabaseType
from ThreadsafeQueue import ThreadsafeQueue
from Logger import Logger
from WebsocketMessageManager import WebsocketMessageManager
from PortManager import PortManager
from RequestHandlers import BaseHandle, AddUserHandler, ContentHandler, createPublicGameHandler, createPrivateGameHandler, loginHandler
import config as cfg


class ServerManager:
    """Class to define a ServerManager. ServerManager handles games and througput"""

    def __init__(self):
        """Init"""
        if not hasattr(ServerManager, 'instance'):
            ServerManager.instance = self
        else:
            self.log("Error: singleton already defined")
            sys.exit(-1)

        self.__running = True
        self.__db = DatabaseManager(DatabaseType.CSV, cfg.db_addr)
        # Instantiate the port manager for all games + admin messages
        self.__port_manager = PortManager(cfg.lower_bound, cfg.upper_bound)
        # Instantiate the message manager exclusively for admin messages
        self.__message_manager = WebsocketMessageManager(cfg.admin)
        self.__pid = os.getpid()
        self.__public_requests = ThreadsafeQueue()
        self.__game_pids = ThreadsafeQueue()
        self.__logger = Logger(cfg.log_addr)
        self.__http_proc = threading.Thread(target=self.serveHTTP)
        self.__pub_polling = threading.Thread(target=self.pollPublic)
        self.log("Server Initialized")
        self.__http_proc.start()
        self.__pub_polling.start()

    def createGame(self, control_port, user_port, private=False):
        """Creates a new thread with a GameController running on it"""
        args = ['createGame.py',
                control_port,
                user_port,
                ]
        if private:
            args.append('--private')
        self.log("Generating new game instance")
        pid = os.spawnlp(os.P_NOWAIT, './createGame.py', args, '--user1=%s')
        self.addPid(pid)
        self.log("Calved game instance at pid:%d" % pid)
        return True

    def addPid(self, pid):
        """Adds a game PID to a list of the current list of process IDs"""
        self.__game_pids.push(pid)

    def checkUser(self, uname, passwd):
        """Checks if a Users is in the database through DatabaseManager"""
        return self.__db.queryForUser(uname, passwd)

    def addUser(self, uname, passwd):
        """Adds a User to the Database through DatabaseManager"""
        return self.__db.addUser(uname, passwd)

    def deleteUser(self, uname, passwd):
        """Removes a User from the Database through DatabaseManager"""
        return self.__db.deleteUser(uname, passwd)

    def requestPublicGame(self, user):
        """Adds a User to the Public game queue"""
        self.__public_requests.push(user)
        return True

    def requestPrivateGame(self, user):
        """Requests the creation of a new Private game"""
        port = self.openPrivateGame(user)
        return port

    def openPublicGame(self, user1=None, user2=None):
        """Creates a new public game with two users from the user queue"""
        if user1 is None:
            self.log("Requesting user for game...")
            user1 = self.__public_requests.pop(block=True)
            self.log("...Got %s" % user1)
        if user2 is None:
            self.log("Requesting user for game...")
            user2 = self.__public_requests.pop(block=True)
            self.log("...Got %s" % user2)

        control = self.__port_manager.getPort()
        if control == -1:
            # No ports available
            self.log("Cannot open public game: No ports available for control")
            return None
        user = self.__port_manager.getPort()
        if user == -1:
            # No ports available
            self.log("Cannot open public game: No ports available for user")
            return None
        self.createGame(control, user, private=False)

        return True

    def openPrivateGame(self, user1, user2=None):
        """Creates a new private game from the request of a user"""
        p = self.__port_manager.getPort()
        if p == -1:
            # No ports available
            self.log(
                "Cannot open private game for user %s: No ports available" % user1)
            return None
        self.createGame(p, user1, user2, private=True)
        return p

    def pollPublic(self):
        """Polls for users in the public queue"""
        self.log("Initialized Polling Thread")
        while self.isRunning():
            p = self.openPublicGame()
            time.sleep(0.01)
            self.log(p)
        self.log("Terminated Polling Thread")

    def isRunning(self):
        """Indicates if the server is running"""
        return self.__running

    def killGame(self, pid=None):
        """Kills a game given a PID and removes the PID from __game_pids"""
        MAXATTEMPTS = cfg.MAXATTEMPTS
        # If the process can't be killed, reports
        r = True
        if not pid is None:
            r &= self.__game_pids.remove(pid)
        else:
            pid = self.__game_pids.pop()
            r &= not pid is None

        if not r:
            self.log("PID not valid- pid:%d" % (pid))
            return False
        else:
            os.kill(pid, signal.SIGINT)
            _, status = os.waitpid(pid)
            attempts = 0
            while not os.WIFSTOPPED(status) and attempts < MAXATTEMPTS:
                attempts += 1
                time.sleep(0.01)
                os.kill(pid, signal.SIGINT)
                _, status = os.waitpid(pid)
            if attempts == MAXATTEMPTS:
                self.log("Aborting pkill(2) pid:%d after %d attempts" %
                         (pid, attempts))
                return False
            self.log("Successfully killed pid:%d" % (pid))
            return True

    def log(self, msg):
        """Logs a message"""
        self.__logger.log(msg)

    def CLIinit(self):
        """Inits the Server menu"""
        menStr = "CheckMate Server: v" + str(cfg.version_number)
        sub = "Server Administration Interface"
        menu = cursesmenu.CursesMenu(menStr, sub)
        killGame = cursesmenu.FunctionItem(
            "Kill a Game[pid]", self.killGame, ['00000'])
        haltServ = cursesmenu.FunctionItem("Halt server", self.halt, None)
        db_admin = cursesmenu.SelectionMenu(["Add user", "Delete user"])
        submenu_item = cursesmenu.SubmenuItem(
            "Database Administration", db_admin, menu)
        serv_admin = cursesmenu.SelectionMenu(
            ["Server Config", "Server Control"])
        submenu_item2 = cursesmenu.SubmenuItem(
            "Server Administration", serv_admin, menu)
        menu.append_item(killGame)
        menu.append_item(submenu_item)
        menu.append_item(submenu_item2)
        menu.append_item(haltServ)
        menu.show()

    def halt(self):
        """Halts the server, killing all open games"""
        if not self.isRunning():
            self.log("Error: Tried to halt a server before it started")
            return False
        self.__running = False
        self.__aio_loop.close()
        while self.__game_pids.size() > 0:
            self.killGame()

        self.__http_proc.join()
        self.__pub_polling.join()

        return True

    def serveHTTP(self):
        """Serves HTTP endpoints"""
        BaseHandle.game_manager = self

        self.__aio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.__aio_loop)
        endpoints = [(r"/addUser", AddUserHandler),
                     (r"/", ContentHandler),
                     (r"/createPublicGame", createPublicGameHandler),
                     (r"/createPrivateGame", createPrivateGameHandler),
                     (r"/login", loginHandler),
                     (r"/about", descriptionHandler)
                     ]
        dblist = tornado.web.Application(endpoints, debug=cfg.debug)
        dblist.listen(cfg.web_test)
        tornado.ioloop.IOLoop.current().start()
