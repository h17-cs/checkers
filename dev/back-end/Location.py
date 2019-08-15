# Class representing a location on the game board
# Created: 08/14
# Author: Charles Hill
# Edited: 08/14 (by Charles)
# Complies to Requirements:
#   - R2.1
#   - R2.4
#   - R2.5
#   - R2.7

class Location:
    def __init__(self, index):
        # Defines a location on the game board, translatable into either an...
        #   R2.1- X,Y coordinate representing location on a 8x8 64-square board
        #   R2.5- index representing which of the 32 playable tiles the location represents
        self.index = index;
    
    def toXYcrd(self):
        # translates a piece's R2.5 index into a R2.1 X,Y board coordinate
        return Location.toXYcrd(self.index);

    def toXYcrd(index):
        # translates a piece's R2.5 index into a R2.1 X,Y board coordinate
        # These are the game indeces laid out on an 8x8 grid.
        # The 2-digit numbers correspond to dark tiles
        # The empty spaces correspond to light tiles
        # __00__01__02__03
        # 04__05__06__07__
        # __08__09__10__11
        # 12__13__14__15__
        # __16__17__18__19
        # 20__21__22__23__
        # __24__25__26__27
        # 28__29__30__31__

        rowind = (index-1) / 4;
        colind = (index-1 % 4) * 2;

        if (rowind % 2) == 0:
            colind+=1;

        return rowind, colind;

    def toIndex(self):
        # translates a piece's R2.1 X,Y board coordinate into a R2.5 index
        return self.index;

    def toIndex(row, col):
        # translates a piece's R2.1 X,Y board coordinate into a R2.5 index
        return 1 + col/2 + 4*row;