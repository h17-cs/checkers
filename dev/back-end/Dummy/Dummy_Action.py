# Class wrapping player actions
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from enum import Enum
from DummyWrap import dummy

class ActionType(Enum):
    # Describes the type of action. Options are:
    #   - Move, an ordinary move as described by R4.2.2 and R4.2.4
    Move = 1
    #   - Capture, a capturing move as described by R4.3.1 and 4.3.3
    Capture = 2
    #   - Draw, a mutual ending of the game as defined by R4.6.1
    Draw = 3
    #   - Forfeit, a resignation of the game as defined by R4.7
    Forfeit = 4
    #   - Save, a mutual stay of game as defined by R4.8
    Save = 5

class Action:
    # Defines a player action, and houses relevant action data
    @dummy
    def __init__(self, actionType, actionData):
        self.__actionType = actionType
        self.__actionData = actionData

    @dummy
    def getType(self):
        # Returns the type of the action
        return 0

    @dummy
    def getData(self):
        # Returns the data associated with the action
        return None

    @dummy
    def setData(self, newData):
        # Sets the action data
        pass

