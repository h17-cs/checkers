
import socket
import threading
from enum import IntEnum
from Message import Message, MessageType
from DummyWrap import dummy


class SocketManager:
    """ Class to manage use of pure sockets"""

    def __init__(self, listenport):
        """ Create new SocketManager"""
        self.__port = listenport
        self.__halted = False
        self.__users = {}
        self.__worker = threading.Thread(target=self.listen)
        self.__worker.start()

    def listen(self):
        """ Listen on socket"""
        s = socket.socket()
        s.bind(('', self.__port))
        s.listen(5)

        while not self.halted():
            c, addr = s.accept()

            self.onconnect(c, addr)

    def message(self, addr, port, msg):
        """ Send a message through a socket"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr, port))
        s.send(msg)
        s.close()

    def query(self, addr, port, msg):
        """query the user through a socket"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((addr, port))
        s.send(msg)
        resp = s.recv(2048)
        s.close()
        return resp

    def halt(self):
        """ Safely stop a socket"""
        if not self.halted():
            self.__halted = True
            self.onhalt()

    def halted(self):
        """ if a socket is stopped """
        return self.__halted

    @dummy
    def onconnect(self, c, addr):
        """ perform an action when a client connects"""
        c.close()

    @dummy
    def onhalt(self):
        """ perform an action when the socket stops"""
        pass


class ControlSocket(SocketManager):
    """ Socket to control sprawling sockets"""
    class ControlCode(IntEnum):
        """ Codes to determine socket state"""
        Status = 0
        Halt = 1

    def __init__(self, port):
        """ Create a new control socket"""
        super().__init__(port)
        self.__listeners = []

    def addListener(self, l):
        """ Add a listener to the ControlSocket"""
        self.__listeners.append(l)

    def onconnect(self, c, addr):
        """ Perform an action on connect"""
        code = c.recv(1)
        msg = "Unknown code (%d)" % code
        if code == ControlSocket.ControlCode.Status or \
                code == ControlSocket.ControlCode.Halt:
            msg = "\n".join(l.flag(code) for l in self.__listeners)

        c.send("%s\n" % msg)
        c.close()


class AdminSocket(SocketManager):
    """ Socket to contact the ServerManager"""

    def __init__(self, port):
        """ Create a new AdminSocket"""
        super().__init__(port)
        self.__svinst = None

    def linkServer(self, server):
        """ Link the AdminSocket to the ServerManager instance"""
        self.__svinst = server

    def onconnnect(self, c, addr):
        """ Perform an action when connect"""
        pass
