# Class moderating the movement of pieces
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)
# Complies to Requirements:

from DummyWrap import dummy


class MovementController:
    # Validates, discovers, and defines the movement of pieces

    @dummy
    def __init__(self, attachedPiece):
        self.attachedPieces = None

    @dummy
    def discoverMoves(self):
        # Discover all available moves of a piece as listed in R1.4.1
        return []
