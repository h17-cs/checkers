# Threadsafe class representing a priority buffer (buffer that prioritizes high-traffic entries)
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import time
import threading


class PriorityBuffer:
    """ PriorityBuffer class used for database writing"""
    UpdateDecay = .98
    ResortEvery = 20

    class PriorityBufferEntry:
        """ Single entry in the PriorityBuffer"""

        def __init__(self, entry):
            """ Create a new PriorityBufferEntry"""
            self.__entry = entry
            self.__count = 1.0

        def getCount(self):
            """ Get the entry count"""
            return self.__count

        def getEntry(self):
            """ Get the entry value"""
            return self.__entry

        def increment(self):
            """ Increment the count"""
            self.__count += 1.0

        def decay(self, coeff):
            """ Decay the count (de-prioritize)"""
            self.__count *= coeff

    def __init__(self, size, debuffer=None):
        """ Create a new PriorityBuffer"""
        self.__buffer = []
        self.__limit = size
        self.__updateCount = 0
        self.__datalock = threading.Lock()
        self.__debuf_fun = debuffer

    def calc_overflow_debuffer(self):
        """ In the case of an overflow, how many entries do we debuffer"""
        # return self.size() - self.__limit + 1   # Overflow + 1 (scalar)
        # 10% of the total size (proportional)
        return int(self.size() * .1)

    def add(self, entry):
        """ add an element to the PriorityBuffer"""
        self.update()
        self.__datalock.acquire()

        returnCode = False
        for i in range(self.size()):
            e = self.__buffer[i]
            if e.getEntry() == (entry):
                e.increment()
                returnCode = True

        if returnCode:
            self.__datalock.release()
            return returnCode

        if self.size() >= self.__limit:
            self.__datalock.release()
            self.debuffer(self.calc_overflow_debuffer())
            # And then retry
            return self.add(entry)
        else:
            self.__buffer.append(PriorityBuffer.PriorityBufferEntry(entry))
            returnCode = True

        self.__datalock.release()
        return returnCode

    def debuffer(self, count):
        """ Remove elements from the buffer to the specific output"""
        self.resort()
        self.__datalock.acquire()

        for i in range(count):
            # Debuffer all extra entries
            e = self.__buffer.pop(-1)
            if self.__debuf_fun is not None:
                self.__debuf_fun(e)

        self.__datalock.release()

    def get(self, func=None):
        """ Get from buffer using lambda fnc"""
        if func is None:
            def func(x): return x

        retval = []
        self.__datalock.acquire()
        for i in range(self.size()):
            e = self.__buffer[i]
            if func(e.getEntry()):
                retval.append(e.getEntry())
                e.increment()
        self.__datalock.release()
        return retval

    def size(self):
        """ Size of the PriorityBuffer"""
        return len(self.__buffer)

    def update(self):
        """ Update the PriorityBuffer"""
        self.__datalock.acquire()
        for e in self.__buffer:
            e.decay(PriorityBuffer.UpdateDecay)
        self.__updateCount += 1
        self.__datalock.release()
        if self.__updateCount >= PriorityBuffer.ResortEvery:
            self.resort()

    def resort(self):
        """ Sort the PriorityBuffer"""
        self.__datalock.acquire()
        self.__buffer.sort(
            key=PriorityBuffer.PriorityBufferEntry.getCount, reverse=True)
        self.__updateCount = 0
        self.__datalock.release()
