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
        self.__buff = PriorityBuffer(self.BufferSize, debuffer= lambda x: self.writeTo(x.getEntry()))

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

        r = Record(self.__keysize, self.__fields)
        r.setKey(key)
        r.setFlag(Record.Flag.Filled)
        r.setData(**fields)

        return self.__buff.add(r)

    def remove(self, key, **fields):
        # Removes a user from the database
        rec = self.findAll(key, **fields)

        if rec is None or len(rec) == 0:
            return False
        else:
            for r in rec:
                r.setFlag(Record.Flag.Empty)
            return True

    def exists(self, key, **fields):
        # Check whether any record exists with the given key and fields
        reqtime = time.time()
        findings = None
        while findings is None and time.time() - reqtime < self.RequestTimeout:
            findings = self.__buff.get(Record.match(key, **fields))
            #print(findings,fields)
            if len(findings) == 0:
                findings = self.readFor(key, blocking=False, **fields)
                time.sleep(0.01)

        return findings is not None and len(findings) > 0

    def findAll(self, key, **fields):
        # Return all records corresponding to the key and field criteria
        reqtime = time.time()
        findings = buffered = None
        while findings is None and time.time() - reqtime < self.RequestTimeout:
            buffered = self.__buff.get(Record.match(key, **fields))
            findings = self.readFor(key, blocking=False, **fields)
            time.sleep(0.01)

        if findings is None:
            findings = []
        findings.extend(buffered)
        return findings

    def readFor(self, key, blocking=True, **fields):
        # Reads database to find records, then returns the given record
        # Accesses DB File, so must aquire file lock
        acquired = self.__datalock.acquire(blocking=blocking)
        if not acquired:
            return None

        matches = []
        match = Record.match(key, **fields)
        f = open(self.__dbpath,'r')
        for line in f:
            r = Record.parse(line,self.__fields)
            if r.getFlag() == Record.Flag.Filled and match(r):
                matches.append(r)
        f.close()
        self.__datalock.release()
        for m in matches:
            self.__buff.add(m)
        return matches

    def writeTo(self, record):
        # Writes record to DB, inserting in same spot if a record with the same key already exists
        # Accesses DB File, so must aquire file lock
        self.__datalock.acquire()
        f = open(self.__dbpath,'r+')
        firstEmpty = -1
        bytesRead = 0
        found = False
        for line in f:
            lineSize = len(line) + 1
            bytesRead += lineSize
            r = Record.parse(line,self.__fields)
            if firstEmpty < 0 and r.getFlag() == Record.Flag.Empty:
                firstEmpty = bytesRead - lineSize

            if r == record:
                f.seek(bytesRead-lineSize)
                found = True
                break

        if not found and firstEmpty != -1:
            f.seek(firstEmpty)

        f.write("%s\n"%(record))
        f.close()
        self.__datalock.release()

        return True

    def flush(self):
        self.__buff.debuffer(self.__buff.size())