# Class for managing back-end server operations
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from DatabaseManager import DatabaseManager, DatabaseType
from MessageManager import MessageManager
from GameController import GameController
from PortManager import PortManager
import config as cfg
import argparse
import os,sys,time,threading
import configparser
from cursesmenu import *
from cursesmenu.items import *
from RequestHandlers import AddUserHandler
import tornado.ioloop
import tornado.web

class ServerManager:
    def __init__(self):
        self.__db = DatabaseManager(DatabaseType.CSV, cfg.db_addr)

        # Instantiate the port manager for all games + admin messages
        self.__port_manager = PortManager(cfg.lower_bound, cfg.upper_bound)

        # Instantiate the message manager exclusively for admin messages
        self.__message_manager = MessageManager(5506)



    def runGame():
        gc = GameController()
    @dummy
    def addUser(self, uname, passwd):
        return True
        #return self.__db.addUser(uname,passwd)

    @dummy
    def deleteUser(self, uname, passwd):
        return True

    @dummy
    def openPublicGame(self, user1, user2):
        game = GameController()
        return True

    @dummy
    def openPublicGame(self):
        return True

    @dummy
    def openPrivateGame(self, user1):
        return True

    @dummy
    def killGame(self, pid):
        return True

    def run(self, useCLI):
        print("Use cli")
        print(useCLI)
        if (useCLI):

            # Do other init tasks...
            # ...
            # ...

            menStr = "CheckMate Server: v" + str(cfg.version_number)
            sub = "Server Administration Interface"
            menu = CursesMenu(menStr, sub)
            menu_item = MenuItem("Menu Item")
            killGame = FunctionItem("Kill a Game[pid]", input, ["Enter a PID"])
            db_admin = SelectionMenu(["Add user", "Delete user"])
            submenu_item = SubmenuItem("Database Administration", db_admin, menu)
            serv_admin = SelectionMenu(["Server Config", "Server Control"])
            submenu_item2 = SubmenuItem("Server Administration", serv_admin, menu)
            menu.append_item(killGame)
            menu.append_item(submenu_item)
            menu.append_item(submenu_item2)

            # Blocks the rest
            menu.show()

    @dummy
    def halt(self):
        return True

    def serveHTTP(self):
        dblist = tornado.web.Application([(r"/", AddUserHandler),])
        dblist.listen(8080)
        tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
     current_path = os.path.abspath(os.path.dirname(sys.argv[0]))
     config = configparser.ConfigParser()

     # Parse command line arguments
     parser = argparse.ArgumentParser()

     # Required arguments

     parser.add_argument(
        "-q", "--headless", help="Start the ServerManager without a CLI",
     default=False, action="store_true"
     )
     args = parser.parse_args()
     if (args.headless):
         sm = ServerManager()
         sm.run(False)
         sm.serveHTTP()
     else:
         sm = ServerManager()
         t = threading.Thread(target=sm.serveHTTP, args=())
         sm.run(True)
