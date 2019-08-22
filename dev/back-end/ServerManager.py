# Class for managing back-end server operations
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from DatabaseManager import DatabaseManager
from MessageManager import MessageManager
from GameController import GameController
from PortManager import PortManager
import config

class ServerManager:
    db_addr = "checkers.db"
    @dummy
    def __init__(self):
        self.__db = DatabaseManager(db_addr)

        # Instantiate the port manager for all games + admin messages
        self.__port_manager = PortManager(config.lower_bound, config.upper_bound)

        # Instantiate the message manager exclusively for admin messages
        self.__message_manager = MessageManager()
        
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

    @dummy
    def run(self):
        return True

    @dummy
    def halt(self):
        return True

    @dummy
    def serveHTTP(self, adress):
        return None
sm = ServerManager()
