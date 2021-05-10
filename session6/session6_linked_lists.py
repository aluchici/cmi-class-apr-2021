class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeDouble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

def add_node(crt_node, data):
    new_node = NodeDouble(data)
    
    new_node.next = crt_node.next
    crt_node.next = new_node
    new_node.prev = crt_node

def add_head(llist, data):
    new_node = NodeDouble(data)
    new_node.next = llist.head
    new_node.prev = None

    if llist.head is not None:
        llist.head.prev = new_node
    
    llist.head = new_node


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(10)

    node2 = Node('cmi-bootcamp')
    node3 = Node(232)

    llist.head.next = node2
    node2.next = node3

    crt_node = llist.head
    while (crt_node.data == node3.data):
        print(crt_node.data)
        crt_node = crt_node.next
