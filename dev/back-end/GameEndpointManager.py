""" Class used to abstract endpoint handlers """
import threading


class GameEndpoint:
    """ GameEndpoint object """

    def __init__(self, endpoint, playerport1, playerport2, controlport):
        """ Creates a new Game endpoint """
        self.__endpoint = endpoint
        self.__player1 = playerport1
        self.__player2 = playerport2
        self.__control = controlport

    def getEndpoint(self):
        """ Endpoint accessor """
        return self.__endpoint

    def getControlPort(self):
        """ Control port accessor """
        return self.__control

    def getPlayerPorts(self):
        """ Player port accessor """
        return self.__player1, self.__player2


class GameEndpointManager:
    """ Class for managing GameEndpoint objects """

    def __init__(self):
        """ Create new GameEndpointManager """
        self.__endpoints = {}
        self.__lockobj = threading.Lock()

    def setEndpoint(self, endpoint):
        """ Sets a GameEndpoint object in the dictionary"""
        self.__lockobj.acquire()
        self.__endpoints[endpoint.getEndpoint()] = endpoint
        self.__lockobj.acquire()

    def getEndpoint(self, endpoint):
        """ Pass a unique endpoint string and receive the data"""
        # If endpoint not recognized, you get None
        self.__lockobj.acquire()
        retval = None
        if endpoint in self.__endpoints.keys():
            retval = self.__endpoints[endpoint]
        self.__lockobj.acquire()
        return retval

    def removeEndpoint(self, endpoint):
        """Pass a unique endpoint string and delete the data"""
        # If endpoint not recognized, returns False, else True
        self.__lockobj.acquire()
        retval = False
        if endpoint in self.__endpoints.keys():
            del self.__endpoints[endpoint]
            retval = True
        self.__lockobj.acquire()
        return retval
