# Class for managing back-end server operations
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from DatabaseManager import DatabaseManager
from MessageManager import MessageManager
from GameController import GameController

class ServerManager:
    db_addr = "checkers.db"
    @dummy
    def __init__(self):
        self.__db = DatabaseManager(db_addr)

    @dummy
    def addUser(self, uname, passwd):
        return self.__db.

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