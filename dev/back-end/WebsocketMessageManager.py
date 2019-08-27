# Class for managing socket communications
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)
# test comm
from enum import Enum
from DummyWrap import dummy
from PortManager import PortManager
import threading
import time
import zmq
import socket as s
import uuid
import math
import random
import tornado
import tornado.ioloop
import tornado.web
import tornado.websocket
from zmq.utils.monitor import recv_monitor_message
from Message import Message, MessageType
import config as cfg
import asyncio
'''
class ClientSocketManager:
    def __init__(self, port, endpoint):
        self.__listener = tornado.web.Application([r'/', ]
                                                  [r'/%s'%endpoint, ])

class ClientWebsocketManager
class AdministrativeWebsocketManager
'''


class WebsocketMessageManager:
    def __init__(self, portbind):
        self.__port = portbind
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        #self.__socket.bind("tcp://*:" + str(self.__port));
        self.__endpoint_url = ''.join(random.choice(cfg.dict) for i in range(cfg.endpoint_length))

    def subscribe(self, fun):
        # subscribe an event listener
        # Listeners must be of the form *.function([self], data)
        self.__subfun = sun

    def send(self, message):
        # Send a message to the socket
        self.__socket.send(message.__str__())

    def recv(self):
        # Read a message from the socket
        msg = self.__socket.recv(copy=True)
        return Message.parse(msg)

    # DEPRICIATED: Used to monitor a socket for connections
    def monitorSocket(self, monitor, timer):
        events = cfg.events
        timeout = time.time() + timer
        connected_users = []
        while(monitor.poll() and (time.time() < timeout)):
            event = recv_monitor_message(monitor)
            event.update({'descriptor:': events[event['event']]})
            if ("EVENT_ACCEPTED" in events[event['event']]):
                print("Player connected!")
                connected_users.append(event['value'])
            print("Event: {}".format(event))

    def run(self):
        aio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(aio_loop)
        print("Endpoint URL for WebsocketMessageHandler: /" + str(self.__endpoint_url))
        epurl = "/game/" + self.__endpoint_url + "/(.*)"
        websocket_endpoint = tornado.web.Application([(epurl, WebsocketMessageHandler), ])
        serv = tornado.httpserver.HTTPServer(websocket_endpoint)
        print("PORT: " + str(self.__port))
        serv.listen(self.__port)


class WebsocketMessageHandler(tornado.websocket.WebSocketHandler):
    def get(self):
        print("Get got")

    def open(self, user):
        print("Connection identified")

    def on_message(self, message):
        print('message received:  %s' % message)
        # Reverse Message and send it back
        print('sending back message: %s' % message[::-1])
        self.write_message(message[::-1])

    def on_close(self):
        self.connected_players.pop()
        print("Player disconnected")
