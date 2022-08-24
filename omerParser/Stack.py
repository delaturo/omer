
import Node


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val: Node):
        self.stack.append(val)

    def top(self):
        if self.stack:
            return self.stack.index(self.stack.count-1)
        return None 

    def isEmpty(self):
        return len(self.stack) == 0
        
    def merge(self):
        grapghMergedNode = ""
        for k in self.stack:
            grapghMergedNode += k.graph
        self.stack = []
        mergedNode = Node.Node(grapghMergedNode)
        return mergedNode