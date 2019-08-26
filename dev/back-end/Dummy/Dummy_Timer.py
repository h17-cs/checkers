# Dummy for Timer class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import time
import threading

from DummyWrap import dummy

MIN_TICK=0.01

class Timer:
    @dummy
    def __init__(self, duration, subscriber, subscriber_args=None):
        # Initialize the thread
        self.__lockobj = threading.Lock();
        self.__running = False;
        self.__startTime = time.time();
        self.__duration = duration;
        self.__subscribers = [];

    @dummy
    def begin (self):
        # Begin the timer, initializing a hidden worker thread
        pass

    @dummy
    def getTimeElapsed(self):
        # Return the time elapsed on the timer
        return 0.0

    @dummy
    def getTimeRemaining(self):
        # Return the time left on the timer
        return 0.0

    @dummy
    def isRunning(self):
        # Return whether the timer is still running
        return False

    @dummy
    def wait(self):
        return True;

    @dummy
    def subscribe(self, function, fargs=None):
        return True

    @dummy
    def restart(self):
        pass