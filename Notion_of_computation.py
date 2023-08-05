"""function that takes number as argument and check if it is a prime number
(return 1) or not (return 0)"""

def check_if_prime_number(number):
    for i in range (2, int((number+3)/2)):
        if number%i == 0:
            return False
    return True

for n in range(0, 100):
    print(f'{n} : {check_if_prime_number(n)}')

"""function that takes list as argument and returns reverse list"""

def reverse_list(list):
    size = len(list)
    new_list = [size]
    for i in range(1, size):
        new_list.append(list[size-1-i])
    return new_list

List = [1,2,3,4,5,6]
print(reverse_list(List))

"""function that sort list using selection method"""

def selection_sort(list):
    size = len(list)
    
    for step in range(size):
        min_index = step
        
        for i in range(step+1, size):
            if list[min_index]>list[i]:
                min_index = i
                
        (list[step], list[min_index]) = (list[min_index], list[step])
        
    return list
        
print(selection_sort([2,6,9,5,1]))

"""function that returns factorial of given number"""

def factorial(number):
    if type(number)==int:
        if number > 1:
            return number*factorial(number-1)
        elif number < 0:
            return 0
        else:
            return 1
    else:
        print("wrong data")

# testing 5
print(factorial(5))
# testing 0
print(factorial(0))
# testing -1
print(factorial(-1))
# testing letter
print(factorial('a'))

"""function that returns biggest number in list"""

def finding_max(input_list):
    max_val = input_list[0]
    for i in range(1, len(input_list)):
        if max_val < input_list[i]:
            max_val = input_list[i]
    return max_val

print(finding_max([3, 5, 9, 3, 4, 7, 8]))

""" class that makes queue that has functions that checks if its empty and that
are putting in elements and getting out elements from oldests """

class Queue:
    def __init__(self):
        # we are starting with empty queue
        self.elements = []
        # next place to fill queue
        self.head = 1
        # last place in queue
        self.tail = 0
    # checking if queue contain any elements
    def is_empty(self):
        return self.head == 1 and self.tail == 0
    def put(self, argument):
        self.elements.append(argument)
        self.head = self.head + 1
        self.tail= self.tail + 1
    def get(self):
        if self.is_empty() == False:
            self.get_element = self.elements[0]
            for i in range(0, self.tail - 1):
                (self.elements[i], self.elements[i+1]) = (self.elements[i+1], self.elements[i])
            return self.get_element
        else:
            return False
        
queue = Queue()
print(queue.is_empty())
queue.put(1)
queue.put(2)
queue.put(3)
print(queue.get())
print(queue.is_empty())   

"""function that calculats sum of even numbers form 1 to n"""
def sum_even_numbers(n):
    sum = 0
    for i in range(1, int((n+2)/2)):
        sum = i*2 + sum
    return sum
print(sum_even_numbers(2))

