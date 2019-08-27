# Threadsafe class representing a priority buffer (buffer that prioritizes high-traffic entries)
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import time
import threading


class PriorityBuffer:
    UpdateDecay = .98
    ResortEvery = 20

    class PriorityBufferEntry:
        def __init__(self, entry):
            self.__entry = entry
            self.__count = 1.0

        def getCount(self):
            # Get the entry count
            return self.__count

        def getEntry(self):
            # Get the entry value
            return self.__entry

        def increment(self):
            # Increment the count
            self.__count += 1.0

        def decay(self, coeff):
            # Decay the count (de-prioritize)
            self.__count *= coeff

    def __init__(self, size, debuffer=None):
        self.__buffer = []
        self.__limit = size
        self.__updateCount = 0
        self.__datalock = threading.Lock()
        self.__debuf_fun = debuffer

    def calc_overflow_debuffer(self):
        # In the case of an overflow, how many entries do we debuffer
        # return self.size() - self.__limit + 1   # Overflow + 1 (scalar)
        return int(self.size() * .1)            # 10% of the total size (proportional)

    def add(self, entry):
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
        self.resort()
        self.__datalock.acquire()

        for i in range(count):
            # Debuffer all extra entries
            e = self.__buffer.pop(-1)
            if self.__debuf_fun is not None:
                self.__debuf_fun(e)

        self.__datalock.release()

    def get(self, func=None):
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
        return len(self.__buffer)

    def update(self):
        self.__datalock.acquire()
        for e in self.__buffer:
            e.decay(PriorityBuffer.UpdateDecay)
        self.__updateCount += 1
        self.__datalock.release()
        if self.__updateCount >= PriorityBuffer.ResortEvery:
            self.resort()

    def resort(self):
        self.__datalock.acquire()
        self.__buffer.sort(key=PriorityBuffer.PriorityBufferEntry.getCount, reverse=True)
        self.__updateCount = 0
        self.__datalock.release()
