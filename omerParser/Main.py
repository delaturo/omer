import Node,Stack

def tokenizer(stack: Stack,node: Node):
    if node and node.isAlphaNumeric():
        stack.push(node)
        return tokenizer(stack,node.get(Node.POSITION.RIGHT))
    else:
        if not stack.isEmpty():
            return stack.merge()

def createTestBasedIn(exp):
    if exp:
        s = exp[0]
        node = Node.Node(s)
        cn = createTestBasedIn(exp[1:])
        if cn:
            node.connect(cn, Node.POSITION.RIGHT)
        return node
    return None

root = createTestBasedIn("hola")
stack = Stack.Stack()
root = tokenizer(stack,root)
print(root.graph)
print("done")

    