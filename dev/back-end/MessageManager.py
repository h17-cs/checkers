""" Class for managing socket communications """
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

import time
from zmq.utils.monitor import recv_monitor_message
import zmq
from DummyWrap import dummy
from Message import Message
import config as cfg


class MessageManager:
    """ Abstract way to manage messages """

    def __init__(self, portbind):
        """ Initialze a new message manager """
        self.__port = portbind
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://*:" + str(self.__port))

    def send(self, message):
        """ Send a message to the socket"""
        self.__socket.send(message.__str__())

    def recv(self):
        """ Read a message from the socket"""
        msg = self.__socket.recv(copy=True)
        return Message.parse(msg)

    def monitorSocket(self, monitor, timer):
        """ Monitors a socket for connections """
        events = cfg.events
        timeout = time.time() + timer
        connected_users = []
        while(monitor.poll() and (time.time() < timeout)):
            event = recv_monitor_message(monitor)
            event.update({'descriptor:': events[event['event']]})
            if "EVENT_ACCEPTED" in events[event['event']]:
                print("Player connected!")
                connected_users.append(event['value'])
            print("Event: {}".format(event))
