from enum import Enum
from DummyWrap import dummy
from PortManager import PortManager
import threading
import time
import zmq
from MessageManager import MessageManager
import socket as s
from zmq.utils.monitor import recv_monitor_message
from Message import Message, MessageType
import config as cfg

portman = PortManager(cfg.lower_bound, cfg.upper_bound, "/dev/null")
mesMan = MessageManager("5507")
ctx = zmq.Context.instance()
rep = ctx.socket(zmq.REP)
req = ctx.socket(zmq.REQ)
monitor = req.get_monitor_socket()
t = threading.Thread(target=mesMan.monitorSocket, args=(monitor, 15))
t.start()

# Test
print("bind req")
req.bind("tcp://127.0.0.1:6666")
req.bind("tcp://127.0.0.1:6667")
time.sleep(1)
print("connect rep")
rep.connect("tcp://127.0.0.1:6667")
time.sleep(0.2)
rep.connect("tcp://127.0.0.1:6666")
time.sleep(1)
ctx.term()
