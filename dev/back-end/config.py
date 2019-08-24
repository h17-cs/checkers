# File to store configuration values in case we want to change em
import zmq
import threading
import time


# The lower bound of the port range to use.
lower_bound = 5506

# The upper bound of the port range to use.
upper_bound = 5700

# ZMQ Event types, in case we want to change
events = {}
for name in dir(zmq):
    if name.startswith('EVENT_'):
        val = getattr(zmq, name)
        events[val] = name

# Visual version number because we lazy
version_number = "0.0.1"

# Group member names for ui
names = "Charles, Nick, Idan, Brendan"

# db path
db_addr = "./testdb.csv"

# tornado debug value
debug = False

# Length of endpoint str
endpoint_length=5

dict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
