"""function that calculats sum of even numbers form 1 to n"""
def sum_even_numbers(n):
    sum = 0
    for i in range(1, int((n+2)/2)):
        sum = i*2 + sum
    return sum
print(sum_even_numbers(2))

"""function that checks if number is palindrome"""
def palindrome(number):
    temp_number = number
    rev_number = 0
    while(temp_number>0):
        rev_number = rev_number*10+temp_number%10
        temp_number = temp_number//10
    if number == rev_number:
        return True
    else:
        return False
        
print(palindrome(12321))
print(palindrome(12345))

"""Function that returns n numbers from Fibonacci sequence"""
def fibonacci_sequence(numbers):
    numbers_sum = []
    if numbers > 0:
        numbers_sum = [0]
        if numbers > 1:
            numbers_sum.append(1)
    for i in range(1, numbers-1):
        numbers_sum.append(numbers_sum[i-1]+numbers_sum[i])
    return numbers_sum

print(fibonacci_sequence(0))
print(fibonacci_sequence(2))
print(fibonacci_sequence(7))

"""function that returns perfect numbers from given range of numbers"""
def perfect_numbers(numbers):
    perfect_num = []
    for i in range(1, numbers+1):
        element_sum = 0
        for j in range(1, int(i/2)+1):
            if i%j == 0:
                element_sum = element_sum + j
        if element_sum == i:
            perfect_num.append(i)
    return perfect_num

print(perfect_numbers(1000))

"""function that returns prime numbers from given range of numbers"""
def prime_numbers(numbers):
    pri_numbers = []
    for i in range(1, numbers):
        if_prime = True
        for j in range(2, int(i/2)+1):
            if i%j ==0:
                if_prime = False
                break
        if if_prime:
            pri_numbers.append(i)
    return pri_numbers

print(prime_numbers(100))
