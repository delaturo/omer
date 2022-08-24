from enum import Enum

OPERATOR = ['|', '&', '∗', '+', '−', '∕', '<', '>' ,'∑', '∫', '√', '∈', '∮', '∯' ,'∰']
ALPHANUMERIC = ['θ', 'ɸ', 'ʊ', 'ω', 'λ', 'π', 'σ', 'α', 'β', 'Δ', 'ℇ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q'
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
SPECIALCHAR = ['\'', '^','~', '∞']
SEPARATOR = [',', '.']
GROUP = ['(', ')', '[', ']','{','}']


class POSITION(Enum):
    UP_LEFT = 0,
    UP = 1,
    UP_RIGHT = 2,
    LEFT = 3,
    RIGHT = 4,
    DOWN_LEFT = 5,
    DOWN = 6,
    DOWN_RIGHT = 7

class Node:

    # graph = None
    # context = {}

    def __init__(self, graph):
        self.graph = graph
        self.context = {}

    def connect(self, newNode, position: POSITION):
        success = False
        if type(newNode) == Node:
            self.context[position] = newNode
            success = True
        return success
    
    def get(self, position: POSITION):
        if self.context:
            return self.context[position]
        else:
            return None

    def __checkIfInArray(self,array):
        isInArray = False
        if self.graph in array:
            isInArray = True
        return isInArray

    def isOperator(self) -> bool:
        return self.__checkIfInArray(OPERATOR)

    def isAlphaNumeric(self) -> bool:
        return self.__checkIfInArray(ALPHANUMERIC)

    def isSpecialChar(self) -> bool:
        return self.__checkIfInArray(SPECIALCHAR)

    def isSeparator(self) -> bool:
        return self.__checkIfInArray(SEPARATOR)

    def isGroup(self) -> bool:
        return self.__checkIfInArray(GROUP)

    def match(self,word):
        return False