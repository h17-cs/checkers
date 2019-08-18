# Threadsafe class representing a CSV-style Database
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from enum import Enum
from PriorityBuffer import PriorityBuffer
from RecordCSV import Record

import threading
import time

class CSVDB_Header:
    sizes = {
        "uname" : 16,
        "password" : 32,
        "game_id" : 64
    }
    default = [("password",sizes["password"])]

class CSVDatabase:
    # Class representing a CSV-style database manager
    BufferSize = 1024   # Buffer 2^10 records from file
    RequestTimeout = 10.0

    def __init__(self, dbpath, keysize=None, fields=None):
        self.__dbpath = dbpath
        self.__datalock = threading.Lock()
        self.__buff = PriorityBuffer(self.BufferSize, debuffer=self.writeTo)

        if keysize is None:
            self.__keysize = CSVDB_Header.sizes["uname"]
        else:
            self.__keysize = keysize

        if fields is None:
            self.__fields = CSVDB_Header.default
        else:
            self.__fields = fields

    def add(self, key, **fields):
        # Adds a record to the database
        # If an empty record exists with the same key (uname), update and fill that record 
        # If no record exists with the same key (uname), make and populate a new record
        #   In both of the above, return True
        # If a filled record exists with the same key, return False

        r = Record(self.__keysize, fields)
        r.setKey(key)
        r.setFlag(Record.Flag.Filled)

        return self.__buff.add(Record())

    def remove(self, key, **fields):
        # Removes a user from the database
        rec = self.findAll(key, **fields)

        if rec is None or rec.getFlag() == Record.Flag.Empty:
            return False
        else:
            rec.setFlag(Record.Flag.Empty)
            return True

    def exists(self, key, **fields):
        # Check whether any record exists with the given key and fields
        reqtime = time.time()
        findings = None
        while findings is None and time.time() - reqtime < self.RequestTimeout:
            findings = self.__buff.get(key, Record.match(key, **fields))

            if len(findings) == 0:
                findings = self.readFor(key, blocking=False, **fields)
                time.sleep(0.01)

        return findings is not None and len(findings) > 0

    def findAll(self, key, **fields):
        # Return all records corresponding to the key and field criteria
        reqtime = time.time()

        while time.time() - reqtime < self.RequestTimeout:
            findings = self.readFor(key=key, blocking=False, **fields)

    def readFor(self, key, blocking=True, **fields):
        # Reads database to find records, then returns the given record
        # Accesses DB File, so must aquire file lock
        acquired = self.__datalock.acquire(blocking=blocking)
        if not acquired:
            return None

        matches = []
        match = Record.match(key, fields)
        f = open(self.__dbpath,'r')
        for line in f:
            r = Record.parse(line,self.__fields)
            if r.getFlag() == Record.Flag.Filled and match(r):
                matches.append(r)
        f.close()
        self.__datalock.release()
        for m in matches:
            self.__buff.add(m)
        return retval

    def writeTo(self, record):
        # Writes record to DB, inserting in same spot if a record with the same key already exists
        # Accesses DB File, so must aquire file lock
        self.__datalock.acquire()
        f = open(self.__dbpath,'r+')
        firstEmpty = -1
        found = False
        for line in f:
            lineSize = len(line)
            r = Record.parse(line)
            if firstEmpty < 0 and r.getFlag() == Record.Flag.Empty:
                firstEmpty = f.tell() - lineSize

            if r.equals(record):
                f.seek(-1*lineSize,1)
                found = True

        if not found and firstEmpty != -1:
            f.seek(firstEmpty)

        f.write("%s\n"%(record))
        f.close()
        self.__datalock.release()

        return True