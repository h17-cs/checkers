from Message import *
from SocketManager import *
from GameWebSocket import GameWebSocket

deny = False
soc = None
class dummygame:
    def addUser(self, user, password, c):
        print ("Adding user",user, password)
        soc = c
        return not deny

f = open("gameupdate.json")
payload = "".join(l for l in f)

gs = GameWebSocket(2500)
d = dummygame()
gs.setGame(d)

print("OK!")
