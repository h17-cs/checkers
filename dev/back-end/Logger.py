
import datetime
import threading


class Logger:
    def __init__(self, fname):
        """ Create new logger """
        self.__f = open(fname, 'a')
        self.__lobj = threading.Lock()

    def log(self, msg):
        """ Log message """
        self.__lobj.acquire()
        dt = datetime.datetime.now()
        self.__f.write("[%4d/%2d/%2d %02d:%02d:%02d:%06d] - %s\n" %
                       (dt.year,
                        dt.month,
                        dt.day,
                        dt.hour,
                        dt.minute,
                        dt.second,
                        dt.microsecond,
                        msg)
                       )
        self.__f.flush()
        self.__lobj.release()

    def getFile(self):
        """ File accessor """
        return self.__f
