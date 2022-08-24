from enum import Enum
from turtle import end_fill
import Node

class POSITION(Enum):
    UP_LEFT = 0,
    UP = 1,
    UP_RIGHT = 2,
    LEFT = 3,
    RIGHT = 4,
    DOWN_LEFT = 5,
    DOWN = 6,
    DOWN_RIGHT = 7

class NodeConnection:
    node = None
    position = None

    def __init__(self, node = None, position = None):
        if type(node) == Node:
            self.node = node
        if type(position) == POSITION:
            self.position