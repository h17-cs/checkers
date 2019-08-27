#!/usr/bin/env python3
from random import shuffle
from time import sleep
from GameController import GameController
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("control_port", type=int, help="Communications port for Player 1 binding")
parser.add_argument("client_port", type=int, help="Communications port for Player 1 binding")
parser.add_argument("--private", help="Flag for private lobby", action='store_true')
args = parser.parse_args()

g = GameController(args.control_port, args.client_port, private=args.private)
