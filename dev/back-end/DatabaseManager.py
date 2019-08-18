# Threadsafe class for managing a database of users and games
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from CSVDatabase import CSVDatabase, CSVDB_Header

from enum import Enum
import threading
import time

class DatabaseType(Enum):
    CSV = 1


class DatabaseManager:
    # Class representing a CSV-style database manager
    BufferSize = 1024   # Buffer 2^10 records from file

    def __init__(self, dbtype, dbpath):
        self.__dbtype = DatabaseType.CSV
        self.__dbpath = dbpath
        self.__datalock = threading.Lock()

        self.__db = CSVDatabase(dbpath=dbpath)

    def addUser(self, uname, passwd):
        # Adds a user to the database
        # If an empty record exists with the same key (uname), update and fill that record 
        # If no record exists with the same key (uname), make and populate a new record
        #   In both of the above, return True
        # If a filled record exists with the same key, return False
        if self.__db.exists(uname):
            return False
        else:
            return self.__db.add(key=uname,password=passwd)

    def deleteUser(self, uname, passwd):
        # Removes a user from the database
        if self.queryForUser(uname,passwd):
            return self.__db.remove(key=uname,password=passwd)
        else:
            return False

    def queryForUser(self, uname, passwd=None):
        # Checks that the username, password pair exists in the database
        if passwd is None:
            return self.__db.exists(key=uname)
        else:
            return self.__db.exists(key=uname,password=passwd)

    def flush(self):
        # Flush all buffered data to the file
        self.__db.flush()