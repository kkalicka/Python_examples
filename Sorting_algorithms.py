import random

Random_array = []
for i in range(10): 
    Random_array.append(random.randint(0, 10))

""" Quicksort """

def partition(array, low, high):
    # create piviot as the last element of list
    pivot = array[high]
    # making second poiter, starting on index 0
    i = low - 1
    for j in range(low, high):
        # if element is smaller than pivot
        if array[j] < pivot:
            # change index of second poniter
            i = i + 1
            # swap second pointer with analyzed element
            (array[i], array[j]) = (array[j], array[i])
    # swap second poiter with pivot
    (array[high], array[i+1]) = (array[i+1], array[high])
    # return placement of current pivot index
    return i +1

def myQuickSort(array, low, high):
    if low<high:
        # calculating placement of "middle" poniter
        pi = partition(array, low, high)
        # sorting numbers on the left side of "middle" pointer 
        myQuickSort(array, low, pi-1)
        # sorting numbers on the right side of "middle" pointer
        myQuickSort(array, pi+1, high)
        
# defining exemple list
Data = Random_array
# list before sorting
print(f'Before sorting with Quicksort: {Data}')
size = len(Data) - 1
myQuickSort(Data, 0, size)          
# list after sorting
print(f'After sorting with Quicksort: {Data}')

""" alliteration sorting """
Data = Random_array
print(f'Before sorting with alliteration: {Data}')

for i in range(0, len(Data)-1):
    for j in range(i, len(Data)-1):
        if Data[i]>Data[j]:
            (Data[i], Data[j]) = (Data[j], Data[i])

print(f'After sorting with alliteration: {Data}')

""" Bumble sort """

Data = Random_array
print(f'Before sorting with Bumble sort: {Data}')

for i in range(0, len(Data)-2):
    for j in range(0, len(Data)-i-1):
        if Data[j]>Data[j+1]:
            (Data[j], Data[j+1]) = (Data[j+1], Data[j])
            
print(f'After sorting with Bumble sort: {Data}')

""" Bucket sort """

def myBucketSort(array):
    bucket = []
    
    # Creating buckets
    for i in range(len(array)):
        bucket.append([])
    
    # Inserting elements to their buckets, difference between buckets-10
    for j in array:
        index_b = int(10*j)
        bucket[index_b].append(j) 
        
    # soring elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
        
    index_k=0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[index_k] = bucket[i][j]   
            index_k=index_k+1
    return array
    
array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(myBucketSort(array))

""" Merge sort 
uses A divide and conquer algorithm is a strategy of solving a large problem by

a)breaking the problem into smaller sub-problems
b)solving the sub-problems, and
c)combining them to get the desired output.
"""

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print(f'After sorting with Merge sort: {array}')

""" Insertion sort 
choosing key and fiding placement for it. replacing key by element next to key starting index"""

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

data = [9, 5, 1, 4, 3]
insertionSort(data)
print(f'Sorted Array in Ascending Order:{data}')

""" Selection sort 
choosing minimum and replacing with inreasing index"""
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print(f'Sorted Array in Ascending Order:{data}')
