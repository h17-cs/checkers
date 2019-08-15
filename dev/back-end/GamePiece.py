from enum import enum

class PieceColor(Enum):
    Light = 0
    Dark = 1

class PieceType(Enum):
    Basic = 0
    King = 1

class GamePiece:
    def __init__(self, color, owner, game):
        self.color = color;
        self.owner = owner;
        self.type = PieceType.Basic;
        self.location = None;
        self.game = game;

    def getValidMoves(self):
        # return a list of valid locations for the piece to move to
        return [None];