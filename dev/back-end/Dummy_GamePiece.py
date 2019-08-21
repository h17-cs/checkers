# Dummy code for GamePiece
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from enum import enum
from DummyWrap import dummy

class PieceColor(Enum):
    # Describes the type of the color according to R3.1
    Light = 0
    Dark = 1

class PieceType(Enum):
    # Describes the type of the piece according to R4.2.3
    Basic = 0
    King = 1

class GamePiece:
    # Describes a checkers game piece
    @dummy
    def __init__(self, color, owner, game):
        self.__color = color;
        self.__owner = owner;
        self.__type = PieceType.Basic;
        self.__location = None;
        self.__game = game;

    @dummy
    def getColor(self):
        # Returns the piece color
        return None

    @dummy
    def getOwner(self):
        # Returns the piece owner
        return None

    @dummy
    def getType(self):
        # Returns the piece type
        return None

    @dummy
    def getLocation(self):
        # Returns the piece location
        return None

    @dummy
    def getGame(self):
        # Returns the checkers game associated with the piece
        return None

    @dummy
    def getValidMoves(self):
        # Returns a list of valid locations for the piece to move to
        # Satisfies R1.4.1
        return [];