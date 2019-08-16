# Threadsafe class for managing a database of users and games
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from enum import Enum
import threading
import time

class DatabaseType(Enum):
    CSV = 1
    SQL = 2

class DatabaseManager:

    @dummy
    def __init__(self, dbtype, dbpath):
        self.__dbtype = dbtype
        self.__dbpath = dbpath
        self.__filelock = threading.Lock()
        self.__dbdict = {}
        self.__lasttouched = None

    @dummy
    def addUser(self, uname, passwd):
        # Adds a user to the database
        return True

    @dummy
    def deleteUser(self, uname, passwd):
        # Removes a user from the database
        return True

    @dummy
    def verify(self, uname, passwd):
        # Checks that the username, password pair exists in the database
        return True

    @dummy
    def open(self):
        # Opens the database
        pass

    @dummy
    def flush(self):
        # Flushes the local database to the file
        pass