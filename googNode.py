class Node:


    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a = Node(5)
b = Node(2)
c = Node(7)
d = Node(6)
e = Node(4)
f = Node(8)
g = Node(3)
h = Node(1)

root = a

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

e.left = h

def findGoodNode(node, p_val = 0):
    if(node is not None):
        if p_val==0:
            print("Good Node : ",node.data)
        elif(node.data>=p_val):
            print("Good node : ",node.data)
        findGoodNode(node.left,max(p_val,node.data))
        findGoodNode(node.right,max(p_val,node.data))

findGoodNode(root)
