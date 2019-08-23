# Class for managing socket communications
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

    def __init__(self, portbind):
        self.__port = portbind;
        self.__context = zmq.Context();
        self.__socket = self.__context.socket(zmq.REP);
        self.__socket.bind(self.__port);

    def send(self, message):
        # Send a message to the socket
        self.__socket.send(message.__str__())

    def recv(self):
        # Read a message from the socket
        msg = self.__socket.recv(copy=True)
        return Message.parse(msg);

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