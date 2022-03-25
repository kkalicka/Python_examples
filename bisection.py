import random

#function that sorts elements that are on first dimension of two dimensional array, "array_len" is equal to length of array
def list_sort(list, is_growing, array_len):
    sort_count = 0 #to delete it later, only to find out how many times loops will go 
    for i in range(0, array_len-1):
        #defining a variable that is equal to number of last index in sorted array
        N = array_len -1
        #if line 15 is commented, then it will be normall bubble sorting
        #value is sorted decides if sorted will be from smallest to biggest (when is_growing == True) or from biggest to smallest (when is_growing == False)
        is_sorted = True
        while N > i:
            if (int(is_growing)*2-1)*(list[N][0]) < (int(is_growing)*2-1)*(list[N-1][0]):
                #swaping element on place "list[N][0]"" with element on "list[N][0]""
                temp = list[N][0]
                list[N][0] = list[N-1][0]
                list[N-1][0] = temp
                #swaping element on place "list[N][1]"" with element on "list[N][1]""
                temp = list[N][1]
                list[N][1] = list[N-1][1]
                list[N-1][1] = temp
                #if we did any changes in array in this while loop it means that array is not sorted
                is_sorted = False
            #deleting reapeted numbers:
            elif (int(is_growing)*2-1)*(list[N][0]) == (int(is_growing)*2-1)*(list[N-1][0]):
                list.pop(N)
                #because we delete one element, lenght of array was decresed by 1
                array_len -=1
            N -= 1 
        #if we dont do any changes in previous while loop, we have arladey sorted array -> this operation often reduces number of loops 
        if is_sorted == True:
            break

#finding out if list is sorted in ascending or descending way
def is_list_sort(list, is_growing):
    #defining bool in which we set the information about if array is sorted(is_sorted = True) or not(is_sorted = False)
    is_sorted = True
    for N in range (1, len(list)):
        #for is_sorted == True: int(is_growing)*2-1) == 1
        #for is_sorted == False: int(is_growing)*2-1) == 2
        if (int(is_growing)*2-1)*(list[N]) < (int(is_growing)*2-1)*(list[N-1]):
            #if any 2 items differ inappropriately, we change "is_sorted" to False
            is_sorted = False
    return is_sorted

#finding number in sorted array using bisection, "element" is element that we want to find in our array
def find_number(list, element, is_growing):
    #setting i and j-> setting the boundaries of the ranges, int((i+j)/2) will be a center of our array 
    i = 0
    j = len(list) -1
    #index on which is an element, starting with no index found so starting with index -1(non existing index in our array)
    index_element = -1
    while(j>i):
        #if element is in first half of array:
        if ((element >= list[i][0]) and (element <= list[int((i+j)/2)][0])):
            j = int((i+j)/2)
        #if element is in second half of array:
        else:
            i = int((i+j+1)/2)
    #finding out if "element" is equal to number that is in our array on index [int((i+j)/2)][0]
    if (element == list[int((i+j)/2)][0]):
        index_element = list[int((i+j)/2)][1]
    return index_element   

#setting array lenght
n = 100
#deciding to sort it later from smallest to biggest(is_growing = True)
#if we want to call function "find_number" we have to make "is_growing" equal to True
is_growing = True
#we are choosing  set from which we will later randomize integers for the array (from 0 to variable "r_range")
r_range = 5
#creating ampty array
Tab = []
#setting the elements of the first dimension as a random integer from 0 to a number equal to the variable "r_range" and setting the elements of the second dimension as their index
for i in range(0, n):
    Tab.append([random.randint(0,r_range), i])

#sorting array so we can use funcion "find_number"
print("\nArray in which we will be finding elements")
list_sort(Tab, is_growing, len(Tab))
print(Tab)

#testing if we will find every element from our array
for i in range(0,len(Tab)+1):
    #if find_number(Tab, i, is_growing) is greater than -1 it found element, if it is equal to -1 it didint found element in our array
    print("element ", i, " is on index: ", find_number(Tab, i, is_growing))