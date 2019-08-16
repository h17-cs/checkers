# Threadsafe class that manages active ports and port counts
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from random import randint
import threading

class PortManager:

    def __init__(self, lowerbound, upperbound, logpath):
        self.__portlock = threading.Lock()
        self.__closed = []
        self.__open = range(lowerbound,upperbound+1)

        self.scramble()

    def getPort(self):
        # Acquire any free port, closing it from further use
        self.__portlock.acquire();
        
        port = self.__open.pop();
        self.__closed.append(port);

        self.__portlock.release();

        return port

    def freePort(self, port):
        # Close the given port, freeing it for further use
        self.__portlock.acquire();
        
        try:
            p = self.__closed.index(port);
            self.__closed.pop(p)
            self.__open.append(port)
        except (ValueError e):
            print("Error: port %d not closed"%(port))

        self.__portlock.release();

    def portsAvailable(self):
        # Determine how many ports are available
        self.__portlock.acquire();

        count = len(self.__open);

        self.__portlock.release();

        return count

    def scramble(self):
        # Randomize the port order
        self.__portlock.acquire();

        self.__open = shuffle(self.__open)

        self.__portlock.release();
