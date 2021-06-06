class Node:


    def __init__(self,data):
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


root = a
a.left = b
a.right = c
b.left = d
d.left = e
d.right = f
c.right = g
d.right = h

def levelOrder():
    qu = []
    qu.append(root)
    while(len(qu)>0):
        elem = qu[0]
        qu = qu[1:]
        print("Poped : ",elem.data)
        if(elem.left is not None):
            print("appending :",elem.left)
            qu.append(elem.left)
        if(elem.right is not None):
            print("appending :",elem.right)
            qu.append(elem.right)

def calculateHeight(node):
    if(node is not None):
        height_left = calculateHeight(node.left)
        height_right = calculateHeight(node.right)
        return max(height_left,height_right) + 1
    else:
        return 0

level_node = {}
def levelOfNode(node, level=0):
    if(node is not None):
        level_node[node.data] = level
        levelOfNode(node.left,level+1)
        levelOfNode(node.right,level+1)

def calculateRootToLeafePath(node, sum=0):
    if(node is not None):
        sum+=int(node.data)
        if(node.left is None and node.right is None):
            print("Root to leaf path : ",sum)
        calculateRootToLeafePath(node.left, sum)
        calculateRootToLeafePath(node.right, sum)
    
def countLeafNode(node):
    if(node is not None):
        if(node.left is None and node.right is None):
            return 1
        CL = countLeafNode(node.left)
        CR = countLeafNode(node.right)
        return int(CL) + int(CR)
    else:
        return 0
# print(calculateHeight(root))
# levelOfNode(root)
# print(level_node)
# calculateRootToLeafePath(root)
print(countLeafNode(root))


