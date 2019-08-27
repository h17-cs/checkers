#!/usr/bin/env python3
import argparse
from GameController import GameController


PARSER = argparse.ArgumentParser()

PARSER.add_argument("control_port", type=int,
                    help="Communications port for Player 1 binding")
PARSER.add_argument("client_port", type=int,
                    help="Communications port for Player 1 binding")
PARSER.add_argument(
    "--private", help="Flag for private lobby", action='store_true')
ARGS = PARSER.parse_args()

game_controller = GameController(
    ARGS.control_port, ARGS.client_port, private=ARGS.private)
