import asyncio
import websockets
import time
from Message import Message, MessageType


class GameWebSocket():
    def __init__(self, port):
        self.__port = port
        self.__halted = False
        self.__connections = []
        self.__game = None
        self.__worker = websockets.serve(self.servePlayers, port=port)
        asyncio.get_event_loop().run_until_complete(self.__worker)
        asyncio.get_event_loop().run_forever()

    def setGame(self, g):
        self.__game = g

    async def servePlayers(self, ws, path):
        msg = await ws.recv()
        if self.__halted:
            print("Error: socket halted")
            ws.close()
        print(msg)
        m = Message.parse(msg)
        if m is None:
            ws.send("Invalid Message")
        # if not m.hasField("message_action")
        if m.getType() == MessageType.Text:
            for c in self.__connections:
                await c.send(msg)

        elif m.getType() == MessageType.AccountAdministration:
            act = m.getField("message_action")
            usr = m.getField("username")
            pwd = m.getField("password")
            if act == 0:
                resp = self.__game.addUser(
                    usr, pwd, ws) if not usr is None else False
                if resp:
                    self.__connections.append(ws)
                    await ws.send("Success")
                else:
                    await ws.send("Failed")
                    ws.close()
            else:
                pass
        else:
            time.sleep(0.1)

    def message(self, addr, port, msg):
        async def msgother():
            uri = "%s:%s" % (addr, port)
            async with websockets.connect(uri) as websocket:
                await websocket.send(msg)

        asyncio.get_event_loop().run_until_complete(msgother())

    def query(self, addr, port, msg):
        resp = ""

        async def msgother():
            uri = "%s:%s" % (addr, port)
            async with websockets.connect(uri) as websocket:
                await websocket.send(msg)
                resp = await websocket.recv()

        asyncio.get_event_loop().run_until_complete(msgother())
        return resp

    def halt(self):
        if not self.halted():
            self.__halted = True
            self.onhalt()

    def onhalt(self):
        for c in self.__connections:
            c.send("Connection Closed.")
            c.close()
