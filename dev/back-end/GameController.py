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
from WebsocketMessageManager import WebsocketMessageManager
class GameController:

    def __init__(self, port):
        self.__board = []
        self.__players = []
        self.__currentTurn = PlayerColor.Light
        self.__players = [Player(PlayerColor.Light, None),
                        Player(PlayerColor.Dark, None)]
        #self.__timer = Timer(60.0, GameController.timeout, (self,));
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
        for i in range(32):
            self.__board.append(None)

        for i in range(12):
            self.addPiece(GamePiece(PieceColor.Light,getPlayer[PlayerColor.Light],self), Location(i))
            self.addPiece(GamePiece(PieceColor.Dark,getPlayer[PlayerColor.Dark],self), Location(32-i))

    def registerPlayer(self, playerColor, playerID):
        # Register players to the board
        return self.players[playerColor].associate(playerID);

    def addPiece(self, piece, location):
        # add a piece to the board
        if self.__board[location.toIndex()] is not None:
            print("Attempted to place a piece in a filled square")
            return False
        else:
            self.__board[location.toIndex()] = piece
            piece.setLocation(location)
            return True

    def movePiece(self, piece, location):
        # move a piece
        oldloc = piece.getLocation()
        if self.__board[location.toIndex()] is not None:
            print("Attempted to place a piece in a filled square")
            return False
        else:
            self.__board[location.toIndex()] = piece
            piece.setLocation(location)

        self.log("Moved piece from #%02d to #%02d"%(oldloc.toIndex(), location.toIndex()))
        return True

    def removePiece(self, piece):
        # remove a piece from the game board
        # --DUMMY--
        loc = piece.getLocation();
        retval = False
        if self.__board[loc] is None:
            print("Error: location points to None")
            retval = False
        else:
            self.__board[loc] = None
            retval = True

        self.log("Removed %s piece at #%02d"%("king" if piece.getType() is PieceType.King else "ordinary"), loc.toIndex())
        return retval


    def promotePiece(self, piece):
        # Promote a piece on the game board
        retval = piece.promote()

        self.log("promoted piece at #%0d"%(piece.getLocation().toIndex()))
        return retval

    @dummy
    def queryOtherPlayer(self, sourcecolor, queryFunc):
        # Facilitate a Player-to-Player query
        otherPlayer = self.player_2 if (self.player_1.color == sourcecolor) else self.player_1;
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

    @dummy
    def timeout(self):
        self.__controllock.acquire()

        self.__controllock.release()
        pass

    @dummy
    def log(self, message):
        # Log a message to users and maybe log to a file
        pass

    @dummy
    def run(self):
        print("Running messenger")
        #self.__messenger.run()
