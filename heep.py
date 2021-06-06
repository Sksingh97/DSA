##Heap =====
## 1. It has to be complete binary tree
## 2. either parent<= left, right child
## 3. parent> left and right child

#Rule 1,2 => Min Heap ( min value will be at root)
#Rule 1,3 => Max Heap (max value will be at root)

# Complete Binary tree=>
#     1. Only last level can be partially field
#     2. all nodes are as left as possible (field from left to right without blank spot)
#   Hight => log N
#many operations like(search, insertion, deletion) are related to hight so operation can be performed in logN
# binary tree as array => better approch less code and no need to create classes
# Min Heap

# step for insertion:
# 1. insert the node at last position
# 2. in case property 2/3 violated swap node to fix

# Step to delete
#     1. swap root with last node 
#     2. delete the last node
#     3. swap until property satisfied

a = [0,10]

def getParentIndex(index):
    return index//2


def heapInsert(value):
    global a
    a.append(value)

    current = len(a) - 1
    parent = getParentIndex(current)

    while(current != 1 and a[current]<a[parent]):
        a[current],a[parent]=a[parent],a[current]
        current=parent
        parent=getParentIndex(current)

print(a)
heapInsert(8)
print(a)
heapInsert(15)
print(a)
heapInsert(2)
print(a)