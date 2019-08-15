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

from enum import enum

class PlayerColor(Enum):
    # R2.6- Defines the color of a player
    Light = 0
    Dark = 1

class Player:
    def __init__(self,color,activeGame):
        self.color = color;
        self.userID = None;

    def forfeit(self):
        # Player(this) requested a forfeit
        self.game.forfeit(self);

    def draw(self):
        # Player(this) requested a draw
        self.game.query(self.color, Player.queryDraw);

    def save(self):
        # Player(this) requested a forfeit
        self.game.query(self.color, Player.querySave);

    def queryDraw(self):
        # Ask the user if they wish to draw
        # --DUMMY--
        return False 

    def querySave(self):
        # Ask the user if they wish to save the current game
        # --DUMMY--
        return False
        
    def associate(self, userId):
        if self.userID is None:
            self.userID = userId
            return True
        else return False

    def act(self):
        # --DUMMY--
        pass