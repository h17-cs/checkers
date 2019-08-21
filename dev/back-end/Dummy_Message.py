# Dummy code for Message class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from enum import Enum

class MessageType(Enum):
    Text = 0
    GameUpdate = 1
    GameAdministration = 2
    AccountAdministration = 3

class Message:
    @dummy
    def __init__(self, messageType)
        self.__messageType = None
        self.__messageBody = None

    @dummy
    def resolve(self):
        return ""