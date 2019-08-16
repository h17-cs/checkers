# Dummy code for MessageManager class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from enum import Enum
from DummyWrap import dummy
import threading
import time
import zmq
from Message import Message, MessageType

class MessageManager:
    @dummy
    def __init__(self, portbind):
        self.__port = None
        self.__context = None
        self.__socket = None

    @dummy
    def send(self, message):
        # Send a message to the socket
        pass

    @dummy
    def recv(self):
        # Read a message from the socket
        return None

    @dummy
    def sendGameUpdate(self, *updates):
        # Send a Game Update Message to the socket
        pass

    @dummy
    def sendText(self, textbody):
        # Send a Text Message to the socket
        pass

    @dummy
    def sendGameAdministration(self, *credentials):
        # Send a Game Administration Message to the socket
        pass

    @dummy
    def sendAccountAdministration(self, *credentials):
        # Send an Account Administration Message to the socket
        pass