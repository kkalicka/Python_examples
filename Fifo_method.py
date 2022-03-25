import random

class Fifo_queue:
    # constructor 
    def __init__(self):
        #we will start with empty list named "Elements" 
        #head=0, tail=0 -> full queue; if head = tail+1 -> empty array
        self.head = 1
        self.tail = 0
        self.Elements = [0,0,0,0,0,0,0,0,0]
        #defining what maximum number of items our queue can contain
        self.list_size = len(self.Elements)

    #finding out if queue is empty
    def is_empty(self):
        #return self.Elements == [] -> we dont want list
        return (self.tail+1)%self.list_size == self.head

    #finding out if queue is empty
    def is_full(self):
        return self.tail == self.head

    #getting out last item from queue
    def get(self):
        if (self.is_empty() == False):
            self.tail = (self.tail+1)%self.list_size
            element = self.Elements[self.tail]
            print("function get ", element, "item to stock")
        else:
            print("function get : queue is empty")

    #putting in first empty place specific element
    def put(self, item):
        if (self.is_full() == False):
            #self.Elements.insert(self.head, item) -> old version
            self.Elements[self.head] = item
            print("function put ", item, " item to queue")
            self.head = (self.head+1)%self.list_size
        else:
            print("function put : queue is full")


Queue = Fifo_queue()
Queue.put(1)
Queue.put(2)
Queue.get()

#example of using class "Fifo_queue", test 
for i in range(3, 13):
    #drawn random number from 0 to 10, verification of module is_full anf is empty
    Queue.put(random.randint(0,10)) 
for i in range(3, 13):
    #verification of module is_full anf is empty
    Queue.get()







