# Class representing a player in the checkers game
# Created: 08/14
# Author: Charles Hill
# Edited: 08/14 (by Charles)
# Complies to Requirements:
#   - R1.1
#   - R1.3-5
#   - R2.6
#   - R4.6.1
#   - R4.7
#   - R5.1

from enum import Enum

from DummyWrap import dummy
from Message import *
import time
import asyncio


class PlayerColor(Enum):
    # R2.6- Defines the color of a player
    Light = 0
    Dark = 1


class Player:
    def __init__(self, playerId, handler, activeGame):
        self.__id = playerId
        self.__handler = handler
        self.__game = activeGame
        self.__color = None

    def getID(self):
        # Return player's ID
        return self.__id

    def getGame(self):
        # Return player's active game
        return self.__game

    def getColor(self):
        # Return the player's color
        return self.__color

    def assignColor(self, color):
        # Set the player's color
        self.__color = color

    def forfeit(self):
        # Player(this) requested a forfeit
        self.game.forfeit(self)

    def draw(self):
        # Player(this) requested a draw
        self.game.query(self.color, Player.queryDraw)

    def save(self):
        # Player(this) requested a forfeit
        self.game.query(self.color, Player.querySave)

    @dummy
    def queryDraw(self):
        # Ask the user if they wish to draw
        return False

    @dummy
    def querySave(self):
        # Ask the user if they wish to save the current game
        return False

    def associate(self, userId):
        if self.userID is None:
            self.userID = userId
            return True
        else:
            return False

    def update(self):
        gb = self.getGame().getBoard()
        m = Message(MessageType.GameUpdate)
        m.addField("timestamp", int(time.time()*1000))
        m.addField("turn", self.getGame().getTurn())
        m.addField("clock_expire", int(
            1000*(time.time()+self.getGame().getTimeRemaining())))
        pieces = self.getGame().getPieces()
        m.addField("board_update", {"sqr_%d" % p.getLocation(): (
            p.getColor(), p.getType()) for p in pieces})
        m.addField("possible_moves", self.determineMoves())

        wait = async lambda: await self.__handler.send(m.__str__())
        asyncio.get_event_loop().run_until_complete(wait())

    @dummy
    def determineMoves(self):
        return []

    @dummy
    def act(self):
        resp = None

        async def query():
            resp = await self.__handler.recv()

        self.update()
        asyncio.get_event_loop().run_until_complete(query())

        print resp
