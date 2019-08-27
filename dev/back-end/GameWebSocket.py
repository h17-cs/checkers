import asyncio
import websockets
import Message

class GameWebSocket():
    def __init__(self, port):
        self.__port = listenport
        self.__halted = False;
        self.__connections=[]
        self.__worker = websockets.serve(servePlayers, 'localhost', port);
        asyncio.get_event_loop().run_until_complete(self.__worker)
        asyncio.get_event_loop().run_forever()

    def setGame(self, g):
        self.__game = g

    async def servePlayers(ws, path):
        msg = await ws.recv()
        if self.__halted:
            print("Error: socket halted");
            ws.close()
        print(msg)
        m = Message.parse(msg);
        act = m.getField("message_action")
        if m.getType() == MessageType.AccountAdmin and act is not None and act == 0:
            usr = m.getField("username")
            pwd = m.getField("password")
            resp = self.__game.addUser(usr, pwd, ws) if not usr is None else False
            if resp:
                self.__connections.append(ws);
                ws.send("Success")
            else:
                ws.send("Failed")
                ws.close()
        else:
            ws.close()
        
    def message(self, addr, port, msg):
        async def msgother():
            uri="%s:%s"%(addr,port)
            async with websockets.connect(uri) as websocket:
                await websocket.send(msg)

        asyncio.get_event_loop().run_until_complete(msgother())

    def query(self, addr, port, msg):
        resp = ""
        async def msgother():
            uri="%s:%s"%(addr,port)
            async with websockets.connect(uri) as websocket:
                await websocket.send(msg)
                resp = await websocket.recv()

        asyncio.get_event_loop().run_until_complete(msgother())
        return resp

    def halt(self):
        if not self.halted():
            self.__halted = True;
            self.onhalt()

    def onhalt(self):
        for c in self.__connections:
            c.send("Connection Closed.");
            c.close()
