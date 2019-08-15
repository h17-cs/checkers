# Class representing the logic and control of a checkers game instance
# Created: 08/14
# Author: Charles Hill
# Edited: 08/14 (by Charles)
# Complies to Requirements:
#   - R1.1
#   - R1.3-5
#   - R3.1
#   - R3.3
#   - R4.1.1
#   - R4.2.*
#   - R4.3.1
#   - R4.3.3-6
#   - R4.4
#   - R4.5.*
#   - R4.6.*
#   - R4.7
#   - R4.8
#   - R5.1
#   - R5.12
#   - R6.2.2-3
#   - R6.2.6-7
#   - R6.2.9
#   - R6.2.10
#   - R6.2.11
#   - R6.2.12
#   - R7.2
#   - R7.3
#   - R12.3.3
#   - Complies to Use Cases as defined in the Requirements document

from Timer import Timer
from Player import Player, PlayerColor

class GameController:
    def __init__(self, socket):
        self.board = []
        self.players = []
        self.timer = None;
        self.currentTurn = PlayerColor.Light;
        self.messenger = new MessengeManager(socket);

    def initialize(self):
        # Initialize the game board, place pieces, and start the game
        self.players = [new Player(PlayerColor.Light, None, self),
                        new Player(PlayerColor.Dark, None, self)]
        self.timer = new Timer();

    def registerPlayer(self, playerColor, playerID):
        # Register players to the board
        return self.players[playerColor].associate(playerID);

    def addPiece(self, piece, location):
        # add a piece to the board
        return True;

    def movePiece(self, piece, location):
        # move a piece 
        return True;

    def removePiece(self, piece):
        # remove a piece from the game board
        return True;

    def promotePiece(self, piece):
        # Promote a piece on the game board
        return True;

    def queryOtherPlayer(self, sourcecolor, queryFunc):
        # Facilitate a Player-to-Player query
        otherPlayer = (self.player_1.color == sourcecolor)
            ? self.player_2
            : self.player_1 ;
        result = queryFunc(otherPlayer)

        if result:
            pass
        else:
            pass

        return result

    def isEnded():
        # Determine whether the game is in an end state
        return False