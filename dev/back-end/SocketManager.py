
import socket
import threading
from enum import IntEnum
from Message import Message, MessageType
from DummyWrap import dummy

class SocketManager:
    def __init__(self, listenport):
        self.__port = listenport
        self.__halted = False;
        self.__users = {};
        self.__worker = threading.Thread(target=self.listen);
        self.__worker.start();

    def listen(self):
        s = socket.socket();
        s.bind(('', self.__port));
        s.listen(5);

        while not self.halted():
            c, addr = s.accept();

            self.onconnect(c, addr);

    def message(self, addr, port, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr,port))
        s.send(msg)
        s.close()

    def query(self, addr, port, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr,port))
        s.send(msg)
        resp = s.recv(2048);
        s.close()
        return resp

    def halt(self):
        if not self.halted():
            self.__halted = True;
            self.onhalt()

    def halted(self):
        return self.__halted;

    @dummy
    def onconnect(self, c, addr):
        c.close();

    @dummy
    def onhalt(self):
        pass;

class GameSocket(SocketManager):
    def __init__(self, port):
        super().__init__(port)
        self.__connections=[]

    def setGame(self, g):
        self.__game = g

    def onconnect(self, c, addr):
        m = Message.parse(c.recv(2048));
        act = m.getField("message_action")
        if m.getType() == MessageType.AccountAdmin and act is not None and act == 0:
            usr = m.getField("username")
            resp = g.addUser(usr) if not usr is None else False
            if resp:
                self.__connections.append(c);
            else:
                c.close()

        else:
            c.close()

    def onhalt(self):
        for c in self.__connectios:
            c.send("Connection Closed.");
            c.close()

class ControlSocket(SocketManager):
    class ControlCode(IntEnum):
        Status = 0;
        Halt = 1;

    def __init__(self, port):
        super().__init__(port)
        self.__listeners = []

    def addListener(self, l):
        self.__listeners.append(l)

    def onconnect(self, c, addr):
        code = c.recv(1);
        msg = "Unknown code (%d)"%code
        if code == ControlSocket.ControlCode.Status or code == ControlSocket.ControlCode.Halt:
            msg = "\n".join(l.flag(code) for l in self.__listeners)

        c.send("%s\n"%msg)
        c.close()

class AdminSocket(SocketManager):
    def __init__(self, port):
        super().__init__(port)
        self.__svinst = None

    def linkServer(self, server):
        self.__svinst = server;

    def onconnnect(self, c, addr):
        pass
