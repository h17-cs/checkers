# Class to wrap Client-Server messages and associated data
# Created: 08/15
# Author: Charles Hill
# Edited: 08/15 (by Charles)

from DummyWrap import dummy
from enum import IntEnum
import json

class MessageType(IntEnum):
    Text = 0
    GameUpdate = 1
    GameAdministration = 2
    AccountAdministration = 3
    GameInit = 4

class Message:
    def __init__(self, messageType):
        self.__messageType = messageType
        self.__messageBody = {}

    def __str__(self):
        # Resolve the message to a JSON string
        return json.dumps(
            {
                'message_type' : self.__messageType,
                'body' : self.__messageBody
            } );
    
    def getType(self):
        # Get the message type
        return self.__messageType;

    def getField(self, key):
        # Add a (key, value) pair to the message body
        if key in self.__messageBody.keys():
            return self.__messageBody[key];
        else:
            return None;

    def addField(self, key, value):
        # Add a (key, value) pair to the message body
        self.__messageBody[key] = value;

    def parse(jstring):
        # STATIC: Generate a message from a JSON string
        obj = json.loads(jstring)
        
        mtype = obj['message_type']
        mbody = obj['body']
        
        msg = Message(mtype)
        for key in mbody:
            msg.addField(key, mbody[key])

        return msg
