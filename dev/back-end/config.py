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
