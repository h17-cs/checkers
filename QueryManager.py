from abc import ABCMeta, abstractmethod
class MessageQueue(metaclass=ABCMeta):
    @property
    @abstractmethod
    def port(self):
        raise Exception("Attempting to use an abstract property; pls instantiate")

    @property
    @abstractmethod
    def ipc_port(self):
        raise Exception("Attempting to use an abstract property; pls instantiate")

    @abstractmethod
    def __init__(self):
        print("ig")

class testMQ(MessageQueue):
    self.port = "5506"
    self.ipc_port = "5507"

    def __init__(self):
        print("og")

tmq = testMQ()
print(tmq.port)
