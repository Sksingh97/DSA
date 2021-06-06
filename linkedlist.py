class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node


ten = Node(10)
twenty = Node(20)
thirty = Node(30)
fourty = Node(40)


head = ten
ten.next = twenty
twenty.next = thirty
thirty.next = fourty
fourty.next = None

def print_list():
    current = head
    while(current is not None):
        print(current.data, end=' ')
        current = current.next
    print()

def insert_top(data):
    global head
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node

def insert_at_end(data):
    current = head
    new_node = Node(data)
    while(current.next is not None):
        current = current.next
    current.next = new_node
    new_node.next = None

def insert_at_index(data, index):
    current = head
    new_node = Node(data)
    position = 0
    while(current is not None):
        if(position == index):
            new_node.next = current.next
            current.next = new_node
            break
        else:
            current = current.next
        position = position + 1
print_list()
insert_at_index(25, 1)
print_list()

