# Class representing the logic and control of a checkers game instance
# Created: 08/14
# Author: Charles Hill
# Edited: 08/15 (by Charles)
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

import threading
from enum import Enum
from Timer import Timer
from Player import Player, PlayerColor

from DummyWrap import dummy

class GameController:

    def __init__(self, port):
        self.__board = []
        self.__players = []
        self.__port = port
        self.__currentTurn = PlayerColor.Light;
        self.__messenger = new MessengeManager(socket);
        self.__players = [new Player(PlayerColor.Light, None, self),
                        new Player(PlayerColor.Dark, None, self)]
        self.__timer = new Timer(60.0, GameController.timeout, (self,));
        self.__controllock = threading.Lock()

    def getBoard(self):
        # Game board accessor
        return self.__board

    def getPlayer(self, color):
        # Game board accessor
        return self.__players[color]

    def getBoard(self):
        # Game board accessor
        return self.__board

    @dummy
    def initialize(self):
        # Initialize the game board, place pieces, and start the game
        #--DUMMY--
        pass

    def registerPlayer(self, playerColor, playerID):
        # Register players to the board
        return self.players[playerColor].associate(playerID);

    @dummy
    def addPiece(self, piece, location):
        # add a piece to the board
        # --DUMMY--
        return True;

    @dummy
    def movePiece(self, piece, location):
        # move a piece 
        # --DUMMY--
        return True;

    @dummy
    def removePiece(self, piece):
        # remove a piece from the game board
        # --DUMMY--
        return True;

    @dummy
    def promotePiece(self, piece):
        # Promote a piece on the game board
        # --DUMMY--
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

    @dummy
    def isEnded(self):
        # Determine whether the game is in an end state
        # --DUMMY--
        return False

    def timeout(self):
        self.__controllock.acquire()

    def run(self):