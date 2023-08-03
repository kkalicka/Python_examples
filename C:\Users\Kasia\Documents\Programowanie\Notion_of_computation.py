"""function that takes number as argument and check if it is a prime number (return 1) or not (return 0)"""
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
