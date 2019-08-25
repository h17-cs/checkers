# Class for managing back-end server operations
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import os,sys,time,threading
import configparser
import asyncio
from cursesmenu import *
from cursesmenu.items import *
import tornado.ioloop
import tornado.web

from DummyWrap import dummy
from DatabaseManager import DatabaseManager, DatabaseType
from GameController import GameController
from ThreadsafeQueue import ThreadsafeQueue
from WebsocketMessageManager import WebsocketMessageManager
from PortManager import PortManager
from RequestHandlers import AddUserHandler, ContentHandler, createPublicGameHandler, createPrivateGameHandler, loginHandler
import config as cfg
import argparse

class ServerManager:
    instance = None

    def __init__(self):
        if ServerManager.instance is not None:
            print("Error: singleton already defined")
            sys.exit(-1)
        else:
            ServerManager.instance = self

        self.__db = DatabaseManager(DatabaseType.CSV, cfg.db_addr)
        # Instantiate the port manager for all games + admin messages
        self.__port_manager = PortManager(cfg.lower_bound, cfg.upper_bound)
        # Instantiate the message manager exclusively for admin messages
        self.__message_manager = WebsocketMessageManager(cfg.admin)
        self.__pid = os.getpid()
        self.__headless = False
        self.__public_requests = ThreadsafeQueue()
        self.__game_pids = ThreadsafeQueue()
        self.__headless = False
        self.__running = True
        self.__worker = threading.Thread(target=self.run)
        self.__polling = threading.Thread(target=self.pollPublic)

    def createGame(self, port1, port2, user1, user2=None, private=False):

        args = [    'createGame.py',
                    port1,
                    port2,
                    user1,
                    user2,
               ]
        if private:
            args.append('--private')
        pid = os.spawnlp(os.P_NOWAIT, 'createGame.py', args, '--user1=%s')
        self.addPid(pid)
        return True

    def addPid(self, pid):
        # Add a pid to the internal list of game process IDs
        self.__game_pids.push(pid)

    def addUser(self, uname, passwd):
        # Add a user from the database
        return self.__db.addUser(uname,passwd)

    def deleteUser(self, uname, passwd):
        # Remove a user from the database
        return self.__db.deleteUser(uname,passwd)

    def openPublicGame(self, user1=None, user2=None):
        # Open a public game. If no users are specified, pop some from queue
        if user1 is None:
            user1 = self.__public_requests.pop(block=True)
        if user2 is None:
            user2 = self.__public_requests.pop(block=True)

        p = self.__port_manager.getPort()
        if p == -1:
            # No ports available
            print("Cannot open public game: No ports available")
            return None
        self.createGame(p, user1, user2, private=False)
        return p

    def openPrivateGame(self, user1, user2=None):
        p = self.__port_manager.getPort()
        if p == -1:
            # No ports available
            print("Cannot open private game for user %s: No ports available"%user1)
            return None
        self.createGame(p, user1, user2, private=True)
        return p

    def pollPublic(self):
        print("Not implem")

    def isRunning(self):
        # Indicates whether or not the server is running
        return self.__running

    def killGame(self, pid):
        # Kills the game associated with the given PID.
        # If the process can't be killed, reports
        if (not self.__headless):
            pid = input("Enter a pid")
            pid = int(pid)
        r = self.__game_pids.remove(pid)
        if not r:
            print("PID not valid- pid:%d"%(pid))
            return False
        else:
            os.kill(pid,signal.SIGINT)
            _, status = os.waitpid(pid)
            attempts = 0
            while not os.WIFSTOPPED(status) and attempts < MAXATTEMPTS:
                attempts+=1
                time.sleep(0.01)
                os.kill(pid,signal.SIGINT)
                _, status = os.waitpid(pid)
            if attempts == MAXATTEMPTS:
                self.log("Aborting pkill(2) pid:%d after %d attempts"%(pid,attempts))
                return False
            self.log("Successfully killed pid:%d"%(pid))
            return True

    @dummy
    def log(self, msg):
        pass

    def run(self, useCLI):
        print("Use cli")
        print(useCLI)
        if (useCLI):
            self.__headless = False
            menStr = "CheckMate Server: v" + str(cfg.version_number)
            sub = "Server Administration Interface"
            menu = CursesMenu(menStr, sub)
            menu_item = MenuItem("Menu Item")
            killGame = FunctionItem("Kill a Game[pid]", self.killGame, ['00000'])
            db_admin = SelectionMenu(["Add user", "Delete user"])
            submenu_item = SubmenuItem("Database Administration", db_admin, menu)
            serv_admin = SelectionMenu(["Server Config", "Server Control"])
            submenu_item2 = SubmenuItem("Server Administration", serv_admin, menu)
            menu.append_item(killGame)
            menu.append_item(submenu_item)

            menu.append_item(submenu_item2)
            menu.show()

    @dummy
    def halt(self):
        return True

    def serveHTTP(self):
        aio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(aio_loop)
        endpoints = [ (r"/addUser", AddUserHandler), (r"/", ContentHandler), (r"/createPublicGame", createPublicGameHandler), (r"/createPrivateGame", createPrivateGameHandler), (r"/login", loginHandler),]
        dblist = tornado.web.Application(endpoints, debug=cfg.debug)
        dblist.listen(cfg.web_test)
        tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    current_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    config = configparser.ConfigParser()

    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q", "--headless", help="Start the ServerManager without a CLI",
        default=False, action="store_true"
     )
    args = parser.parse_args()
    if (args.headless):

        # NOTE: All for testing below.

        sm = ServerManager()
        sm.run(False)
        t = threading.Thread(target=sm.serveHTTP, args=())
        t.start()
        # game2 = GameController(5508)
        # t2 = threading.Thread(target=game2.run, args=())f
        # t2.start()
    else:
        sm = ServerManager()
        t = threading.Thread(target=sm.serveHTTP, args=())
        sm.run(True)
