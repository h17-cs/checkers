# Dummy code for PortManager class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from random import randint
import threading

class PortManager:
    @dummy
    def __init__(self, lowerbound, upperbound, logpath):
        self.__portlock = threading.Lock()
        self.__closed = []
        self.__open = []

    @dummy
    def getPort(self):
        # Acquire any free port, closing it from further use
        return None

    @dummy
    def freePort(self, port):
        # Close the given port, freeing it for further use
        pass

    @dummy
    def portsAvailable(self):
        # Determine how many ports are available
        return 0

    @dummy
    def scramble(self):
        # Randomize the port order
        pass