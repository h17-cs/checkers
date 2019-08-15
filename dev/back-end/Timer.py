# Class wrapping timed functions with event subscribers
# Created: 08/14
# Author: Charles Hill
# Edited: 08/14 (by Charles)

import time
import threading

MIN_TICK=0.01

class Timer:
    def __init__(self, duration, subscriber):
        # Initialize the thread
        self.lockobj = threading.Lock();
        self.running = False;
        self.startTime = time.time();
        self.duration = duration;
        self.subscribers = [];
        self.subscribers.append(subscriber);

    def begin (self):
        # Begin the timer, initializing a hidden worker thread
        t = threading.Thread(target=Timer.wait,name="Timer Helper Thread",args=(self,));
        self.running = True
        t.start();

    def getTimeElapsed(self):
        # Return the time elapsed on the timer
        return time.time() - self.startTime;

    def getTimeRemaining(self):
        # Return the time left on the timer
        return self.duration - self.getTimeElapsed()

    def wait(self):
        if not self.running:
            print("Attempted to wait on a dead worker.\n");
            return False;
        elapsed = 0.0;
        n = 0;
        while elapsed < self.duration:
            if self.lockobj.acquire(False):
                n = 0;
                elapsed = self.getTimeElapsed();
                self.lockobj.release();
            else print("\rMissed %d lock attempt(s)\r", ++n);
            sleep(MIN_TICK);
        self.lockobj.acquire()
        self.running = False
        self.lockobj.release()

        for f in self.subscribers:
            f();

        return True;

    def subscribe(self, function):
        self.lockobj.acquire()
        if not running:
            self.lockobj.release()
            return False
        self.subscribers.append(function)
        self.lockobj.release()
        return True

    def restart(self, function):
        self.lockobbj.acquire()
        self.startTime = time.time()
        if not self.running:
            self.begin()
        self.lockobj.release()