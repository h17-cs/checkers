# Threadsafe class representing a Record in a CSV database
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from enum import Enum
import threading

class Record:
    class Flag(Enum):
        Filled = True
        Empty = False

    class FlagChar(Enum):
        Filled = '#'
        Empty = '-'

    def __init__(self, keysize, fields=None):
        self.__flag = Record.Flag.Empty
        self.__key = ""
        self.__keysize = keysize
        self.__fields = []
        self.__data = {}
        self.__datalock = threading.Lock()

        if fields is not None:
            for field, fieldsize in fields:
                self.appendField(field, fieldsize)

    def appendField(self, field, fieldsize):
        # Add fields to the record
        self.__datalock.acquire()
        self.__fields.append((field,fieldsize))
        self.__data[field] = ''
        self.__datalock.release()

    def setKey(self, key):
        # Set the database entry key
        self.__key = key

    def getKey(self):
        # Get the database entry key
        return self.__key

    def setFlag(self, flag):
        # Set the database entry flag
        self.__flag = flag

    def getFlag(self):
        # Get the database entry flag
        return self.__flag

    def getField(self, field):
        # Get the data corresponding to the field, if the field exists
        self.__datalock.acquire()
        ret_dat = None
        if self.hasField(field):
            ret_dat = self.__data[field]
        self.__datalock.release()
        return ret_dat

    def hasField(self, field):
        # Check if Record has the given field
        return field in [header for header,_ in self.__fields]

    def setData(self, **data):
        # Set multiple Record fields off kwargs param
        self.__datalock.acquire()
        
        for k in data:
            if self.hasField(k):
                self.__data[k] = data[k]

        self.__datalock.release()

    def getData(self):
        # Get the data encoded by this line
        return self.__data

    def getFields(self):
        # Get the field headers for the record
        return self.__fields

    def __eq__(self, other):
        # Compare this entry to another
        # Computationally exhasting, so broken into 3 parts
        #   Note: flags not especially important
        def testKeys():
            # Test the keys
            return self.getKey() == other.getKey()

        def testHeads():
            # Test the field headers
            return all([self.hasField(f) for f,_ in other.getFields()]) \
                and all([other.hasField(f) for f,_ in self.getFields()])

        def testData():
            # Test the field data
            fs = self.getFields()
            return all([self.getField(f) == other.getField(f) for f,_ in fs])

        return testKeys() and testHeads() and testData()


    def __str__(self):
        # generate a string representing the record and all its fields
        data_tail = ""
        fields = []
        self.__datalock.acquire()

        data_tail = ",".join(size for _,size in self.getFields())

        dat = self.getData()
        data_tail = data_tail%(dat[f] for f in fields)

        flag = Record.FlagChar.Filled if self.getFlag() == Record.Filled else Record.FlagChar.Empty
        key = ("%%%ds"%self.__keysize) % self.getKey()
        key_header = "%c,%s"%(flag,key)
        self.__datalock.release()
        return "%s,%s"%(key_header,data_tail)


    def parse(line, fields):
        # Parse a record from a string and headers
        tokens = [t.strip() for t in line.split(',')]
        flag = tokens[0]
        key = tokens[1]
        data = tokens[2:]

        if not len(data) == len(fields):
            print("Field length mismatch in: \n%16s%s\n\t\tvs\n%16s%s\n" % 
                (   "expected:", ",".join(f for f,_ in fields),
                    "data:", ",".join(data)
                    )) 

        r = Record(fields)
        r.setFlag(Record.Flag.Filled if flag == Record.FlagChar.Filled else Record.Flag.Empty)
        r.setKey(tokens[1])
        if tokens[1] is None or len(tokens[1]) == 0:
            r.setFlag(Record.Flag.Empty)

        for i in len(data):
            r.setData(fields[i],data[i])

        return r

    def match(key, **fields):
        def helper(entry):
            if not entry.getKey() == key:
                return False 
            for f in fields:
                if not entry.getField(f) == fields[f]:
                    return False
            return True
        return helper