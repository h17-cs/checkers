# Dummy code for Player class
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from enum import enum

class PlayerColor(Enum):
    # R2.6- Defines the color of a player
    Light = 0
    Dark = 1

class Player:
    @dummy
    def __init__(self,color,activeGame):
        self.color = None;
        self.userID = None;

    @dummy
    def forfeit(self):
        # Player(this) requested a forfeit
        pass

    @dummy
    def draw(self):
        # Player(this) requested a draw
        pass

    @dummy
    def save(self):
        # Player(this) requested a forfeit
        pass

    @dummy
    def queryDraw(self):
        # Ask the user if they wish to draw
        return False 

    @dummy
    def querySave(self):
        # Ask the user if they wish to save the current game
        return False
        
    @dummy
    def associate(self, userId):
        return True

    @dummy
    def act(self):
        pass