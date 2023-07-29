""" Quicksort """
number_of_calculations  = 0
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
Data = [7,8,1,0,9,7]
# list before sorting
print(f'Before sorting with Quicksort: {Data}')
size = len(Data) - 1
myQuickSort(Data, 0, size)          
# list after sorting
print(f'After sorting with Quicksort: {Data}')
print(f'Number of calculations: {number_of_calculations}')

""" alliteration sorting """
Data = [7,8,1,0,9,7]
number_of_calculations = 0
print(f'Before sorting with alliteration: {Data}')

for i in range(0, len(Data)-1):
    for j in range(i, len(Data)-1):
        if Data[i]>Data[j]:
            (Data[i], Data[j]) = (Data[j], Data[i])
        number_of_calculations = number_of_calculations + 1

print(f'After sorting with alliteration: {Data}')
print(f'Number of calculations: {number_of_calculations}')

""" Bumble sort """

Data = [7,8,1,0,9,7]
number_of_calculations = 0
print(f'Before sorting with Bumble sort: {Data}')

for i in range(0, len(Data)-2):
    for j in range(i, len(Data)-2):
        if Data[j]>Data[j+1]:
            (Data[j], Data[j+1]) = (Data[j+1], Data[j])
        number_of_calculations = number_of_calculations + 1

print(f'After sorting with Bumble sort: {Data}')
print(f'Number of calculations: {number_of_calculations}')

""" Bucket sort """

""" Merge sort """