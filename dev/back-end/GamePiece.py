# Class representing a checkers game piece
# Created: 08/14
# Author: Charles Hill
# Edited: 08/15 (by Charles)
# Complies to Requirements:
#   - R1.4.1
#   - R3.1
#   - R4.2.3

from enum import Enum
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
    def __init__(self, color, owner, game):
        self.__color = color;
        self.__owner = owner;
        self.__type = PieceType.Basic;
        self.__location = None;
        self.__game = game;

    def getColor(self):
        # Returns the piece color
        return self.__color

    def getOwner(self):
        # Returns the piece owner
        return self.__owner

    def getType(self):
        # Returns the piece type
        return self.__type

    def getLocation(self):
        # Returns the piece location
        return self.__location

    def getGame(self):
        # Returns the checkers game associated with the piece
        return self.__game

    @dummy
    def getValidMoves(self):
        # Returns a list of valid locations for the piece to move to
        # Satisfies R1.4.1
        # --DUMMY--
        return [None];