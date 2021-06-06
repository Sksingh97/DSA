class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

root = a
a.left = b
a.right = c
b.right = e
b.left = d
e.left = h
e.right = i
c.left = f
c.right = g


def preOrder(node):
    if(node is not None):
        print(node.data, end = " ")
        preOrder(node.left)
        preOrder(node.right)
print()
def inOrder(node):
    if(node is not None):
        inOrder(node.left)
        print(node.data, end = " ")
        inOrder(node.right)
print()
def postOrder(node):
    if(node is not None):
        postOrder(node.left)
        postOrder(node.right)
        print(node.data , end = " ")

print("PreOrder : ")
preOrder(root)
print()
print("inOrder : ")
inOrder(root)
print()
print("postOrder : ")
postOrder(root)
