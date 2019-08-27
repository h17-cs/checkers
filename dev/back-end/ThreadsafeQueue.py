""" Class that wraps a threadsafe queue"""

import threading
import time
import random


class ThreadsafeQueue:
    """ A Threadsafe queue"""

    def __init__(self):
        """ creates a threadsafe queue"""
        self.__queue = []
        self.__lockobj = threading.Lock()

    def push(self, obj):
        """ Appends an object to the threadsafe queue"""
        self.__lockobj.acquire()
        self.__queue.append(obj)
        self.__lockobj.release()

    def pop(self, block=False):
        """ removes the last added element in the threadsafe queue"""
        self.__lockobj.acquire()
        if len(self.__queue) == 0 and not block:
            self.__lockobj.release()
            return None
        elif block:
            while len(self.__queue) == 0:
                self.__lockobj.release()
                time.sleep(0.01)
                self.__lockobj.acquire()

        retval = self.__queue.pop(0)
        self.__lockobj.release()
        return retval

    def remove(self, item):
        """ removes a specific item from the threadsafe queue"""
        self.__lockobj.acquire()
        retval = False
        if item not in self.__queue:
            retval = False
        else:
            self.__queue.remove(item)
            retval = True
        self.__lockobj.release()
        return retval

    def ImFeelingUnlucky(self):
        """ shuffles the threadsafe queue"""
        self.__lockobj.acquire()
        random.shuffle(self.__queue)
        self.__lockobj.release()

    def size(self):
        """ returns the size of the threadsafe queue"""
        self.__lockobj.acquire()
        retval = len(self.__queue)
        self.__lockobj.release()
        return retval
