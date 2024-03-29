"""Class representing the logic and control of a checkers game instance"""
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
from Player import Player, PlayerColor
from DummyWrap import dummy
from GamePiece import PieceType, PieceColor, GamePiece
from Location import Location
from Message import Message
import config as cfg
from SocketManager import ControlSocket
import GameWebSocket as GameSocket


class GameController:

    """ Interface used to control games"""

    def __init__(self, control_port, user_port, private=False):
        self.__board = []
        self.__players = []
        self.__controllock = threading.Lock()
        self.__private = private
        self.__control = ControlSocket(control_port)
        self.__users = GameSocket(user_port)
        self.__users.setGame(self)
        self.__halted = False
        self.__timer = None
        self.__currentTurn = None

    def getBoard(self):
        """ Game board accessor """
        return self.__board

    def getPlayer(self, color):
        """ Game player accessor """
        return self.__players[color]

    def main(self):
        """ Main control flow loop """
        self.__players = [Player(PlayerColor.Light, None),
                          Player(PlayerColor.Dark, None)]
        #self.__timer = Timer(60.0, GameController.timeout, (self,));

    @dummy
    def initialize(self):
        """ Initialize the game board, place pieces, and start the game """
        for i in range(32):
            self.__board.append(None)

        for i in range(12):
            self.addPiece(GamePiece(PieceColor.Light,
                                    getPlayer[PlayerColor.Light], self), Location(i))
            self.addPiece(GamePiece(PieceColor.Dark,
                                    getPlayer[PlayerColor.Dark], self), Location(32-i))

        self.__currentTurn = PlayerColor.Light

    def addUser(self, user, password, c):
        """ Adds a user to the game """
        msg = Message(Message.MessageType.AccountAdministration)
        # Use c var
        print(c)
        msg.addField("message_action", 0)
        msg.addField("username", user)
        msg.addField("password", password)
        resp = self.__control.query("localhost", cfg.admin, msg.__str__())
        if resp == "Success":
            self.__players.append(user)
            return True
        else:
            return False

    def registerPlayer(self, playerColor, playerID, port):
        """ Register players to the board """
        return self.__players[playerColor].associate(playerID, port)

    def playerBind(self, playerId, playerHandler):
        """ Register players to the game """
        self.__controllock.acquire()
        retval = False
        if len(self.__players) < 2:
            self.__players.append(Player(playerId, playerHandler, self))
            retval = True
        self.__controllock.release()
        return retval

    def addPiece(self, piece, location):
        """ add a piece to the board """
        self.__controllock.acquire()
        if self.__board[location.toIndex()] is not None:
            print("Attempted to place a piece in a filled square")
            self.__controllock.release()
            return False
        else:
            self.__board[location.toIndex()] = piece
            piece.setLocation(location)
            self.__controllock.release()
            return True

    def movePiece(self, piece, location):
        """ move a piece """
        self.__controllock.acquire()
        oldloc = piece.getLocation()
        if self.__board[location.toIndex()] is not None:
            print("Attempted to place a piece in a filled square")
            self.__controllock.release()
            return False
        else:
            self.__board[location.toIndex()] = piece
            piece.setLocation(location)
            self.__controllock.release()

            self.log("Moved piece from #%02d to #%02d" %
                     (oldloc.toIndex(), location.toIndex()))
            return True

    def removePiece(self, piece):
        """ remove a piece from the game board """
        loc = piece.getLocation().toIndex()
        self.__controllock.acquire()
        loc = piece.getLocation()
        retval = False
        if self.__board[loc] is None:
            print("Error: location points to None")
            retval = False
            self.__controllock.release()
        else:
            self.__board[loc] = None
            retval = True
            self.__controllock.release()
        log_str = "Removed % s piece" % (
            "king" if piece.getType() is PieceType.King else "ordinary")
        log_str += "at #%02d" % loc
        self.log(log_str)
        return retval

    def promotePiece(self, piece):
        """ Promote a piece on the game board """
        retval = piece.promote()

        self.log("promoted piece at #%0d" % (piece.getLocation().toIndex()))
        return retval

    @dummy
    def queryOtherPlayer(self, sourcecolor, queryFunc):
        """ Facilitate a Player-to-Player query """
        otherPlayer = self.__players[1] if (
            self.__players[0].color == sourcecolor) else self.__players[0]
        result = queryFunc(otherPlayer)

        if result:
            pass
        else:
            pass

        return result

    @dummy
    def isEnded(self):
        """ Determine whether the game is in an end state """
        # --DUMMY--
        return False

    def ready(self):
        """ Determine whether the game is in an end state """
        # --DUMMY--
        return len(self.__players) == 1

    def flag(self, code):
        """ Defines the flag for the controlsocket """
        if code == ControlSocket.ControlCode.Halt:
            self.halt()
            return "Halted"
        elif code == ControlSocket.ControlCode.Status:
            colorcode = "\033[31;0m" if self.isEnded() else "\033[32;0m"
            status = "Dormant" if self.isEnded() else "Active"
            return "Status: [%s%s\033[0m], time remaining: %f" % (colorcode, status, self.__timer.getTimeRemaining())
        else:
            return "Code (%d) not supported" % code

    @dummy
    def log(self, message):
        """ Log a message to users and maybe log to a file """
        pass

    @dummy
    def halt(self):
        """ Halt the game """
        self.__halted = True
        self.log("Game Halted.")
        self.__control.halt()
        self.__users.halt()
