# Dummy code for GameController
# Created: 08/14
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import threading
from enum import Enum
from Timer import Timer
from Player import Player, PlayerColor

from DummyWrap import dummy

class GameController:

    @dummy
    def __init__(self, socket):
        self.__board = []
        self.__players = []
        self.__currentTurn = None
        self.__messenger = None
        self.__players = None
        self.__timer = None
        self.__controllock = threading.Lock()

    @dummy
    def getBoard(self):
        # Game board accessor
        return None

    @dummy
    def getPlayer(self, color):
        # Game board accessor
        return None

    @dummy
    def getBoard(self):
        # Game board accessor
        return None

    @dummy
    def initialize(self):
        # Initialize the game board, place pieces, and start the game
        pass

    @dummy
    def registerPlayer(self, playerColor, playerID):
        # Register players to the board
        return True;

    @dummy
    def addPiece(self, piece, location):
        # add a piece to the board
        return True;

    @dummy
    def movePiece(self, piece, location):
        # move a piece 
        return True;

    @dummy
    def removePiece(self, piece):
        # remove a piece from the game board
        return True;

    @dummy
    def promotePiece(self, piece):
        # Promote a piece on the game board
        return True;

    @dummy
    def queryOtherPlayer(self, sourcecolor, queryFunc):
        # Facilitate a Player-to-Player query
        return True

    @dummy
    def isEnded(self):
        # Determine whether the game is in an end state
        return False

    @dummy
    def timeout(self):
        # Timeout has occured; end the game
        pass