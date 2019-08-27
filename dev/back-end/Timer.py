"""Class wrapping timed functions with event subscribers"""
# Created: 08/14
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import time
import threading

MIN_TICK = 0.01


class Timer:
    """ Create a new timer for turns and game duration"""

    def __init__(self, duration, subscriber, subscriber_args=None):
        """Initialize the thread"""
        self.__lockobj = threading.Lock()
        self.__running = False
        self.__startTime = None
        self.__duration = duration
        self.__subscribers = []
        if not subscriber is None:
            self.subscribe(subscriber, subscriber_args)

    def begin(self):
        """ Begin the timer, initializing a hidden worker thread"""
        if self.isRunning():
            print("Timer already running")
            return False
        t = threading.Thread(
            target=Timer.wait, name="Timer Helper Thread", args=(self,))
        self.__running = True
        self.__startTime = time.time()
        t.start()
        return True

    def getTimeElapsed(self):
        """ Return the time elapsed on the timer"""
        if self.__startTime is None:
            print("Timer hasn't started yet!")
            return -1.0
        return time.time() - self.__startTime

    def getTimeRemaining(self):
        """Return the time left on the timer"""
        return self.__duration - self.getTimeElapsed()

    def isRunning(self):
        """Return whether the timer is still running"""
        return self.__running

    def wait(self):
        """ Await to prevent conflicting lock requests"""
        if not self.isRunning():
            print("Attempted to wait on a dead worker.")
            return False
        elapsed = 0.0
        n = 0
        while elapsed < self.__duration:
            if self.__lockobj.acquire(False):
                n = 0
                elapsed = self.getTimeElapsed()
                self.__lockobj.release()
            else:
                print("\rMissed %d lock attempt(s)\r" % (++n))
            time.sleep(MIN_TICK)
        self.__lockobj.acquire()
        self.__running = False
        self.__lockobj.release()

        for f, fargs in self.__subscribers:
            if fargs is not None:
                f(fargs)
            else:
                f()

        return True

    def subscribe(self, function, fargs=None):
        """ subscribe a function to the timer"""
        self.__lockobj.acquire()
        # if not self.isRunning():
        #    self.__lockobj.release()
        #    return False
        self.__subscribers.append((function, fargs))
        self.__lockobj.release()
        return True

    '''
    def restart(self):
        self.__lockobj.acquire()
        self.__startTime = time.time()
        if not self.isRunning():
            self.begin()
        self.__lockobj.release()
    '''
