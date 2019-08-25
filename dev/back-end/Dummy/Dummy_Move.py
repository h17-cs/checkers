# Dummy code for Move class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy

class Move():
    # Describes the ordinary movement of a piece as defined by R4.2.2 and R4.2.4
    @dummy
    def __init__(self, source, destination, gamePiece):
        self.__source = None
        self.__destination = None
        self.__piece = None
        self.__nextMove = None

    @dummy
    def appendMove(self, nextMove):
        # Appends a move to the current move.
        # If the current move already has an apended move, insert the new move between the two
        pass

    @dummy
    def getPiece(self):
        # Returns the acting piece in the movement
        return None

    @dummy
    def getSource(self):
        # Returns the source location of the move
        return None

    @dummy
    def getDestination(self):
        # Returns the destination location of the move
        return None

    @dummy
    def getNext(self):
        # Returns a move postceding the current move
        return None

class Capture(Move):
    # Describes the capturing movement of a piece as defined by R4.3.1 and R4.3.3
    @dummy
    def __init__(self, source, destination, actingPiece, capturedPiece):
        # Super constructor: Move
        super().__init__(source,destination,actingPiece)
        self.__capturedPiece = None

    @dummy
    def getCapturedPiece(self):
        # Returns the piece captured in the move
        return None