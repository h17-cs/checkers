# Class describing the move of a piece. May be serialized
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)


class Move():
    # Describes the ordinary movement of a piece as defined by R4.2.2 and R4.2.4
    def __init__(self, source, destination, gamePiece):
        # Super constructor: Action
        # super().__init__(self.kind, self)
        self.__source = source
        self.__destination = destination
        self.__piece = gamePiece
        self.__nextMove = None

    def appendMove(self, nextMove):
        # Appends a move to the current move.
        # If the current move already has an apended move, insert the new move between the two
        if not self.__nextMove is None:
            self.__nextMove.appendMove(nextMove)

        self.__nextMove = nextMove

    def getPiece(self):
        # Returns the acting piece in the movement
        return self.__piece

    def getSource(self):
        # Returns the source location of the move
        return self.__source

    def getDestination(self):
        # Returns the destination location of the move
        return self.__destination

    def getNext(self):
        # Returns a move postceding the current move
        return self.__nextMove


class Capture(Move):
    # Describes the capturing movement of a piece as defined by R4.3.1 and R4.3.3
    def __init__(self, source, destination, actingPiece, capturedPiece):
        # Super constructor: Move
        super().__init__(source, destination, actingPiece)
        self.__capturedPiece = capturedPiece

    def getCapturedPiece(self):
        # Returns the piece captured in the move
        return self.__capturedPiece
