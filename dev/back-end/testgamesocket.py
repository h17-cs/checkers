from Message import *
from SocketManager import *

deny = False
soc = None
class dummygame:
    def addUser(self, user, password, c):
        print ("Adding user",user, password)
        soc = c
        return not deny

f = open("gameupdate.json")
payload = "".join(l for l in f)

gs = GameSocket(2500)
d = dummygame()
gs.setGame(d)
