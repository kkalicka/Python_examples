class Node:
    def __init__(self, data):
        self.data_val = data
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def append_item(self, item):
        New_node = Node(item)
        New_node.next= self.head
        if self.head != None:
            self.head.prev = New_node
        self.head = New_node
        
    def print_list(self, node):
        while(node is not None):
            print(node.data_val)
            node = node.next

double_l = DoubleLinkedList()
double_l.append_item(2)
double_l.append_item(3)
double_l.append_item(2)
double_l.print_list(double_l.head)