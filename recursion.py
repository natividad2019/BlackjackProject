# Recursion in Python


# Function creating
# Function calling


# def my_function():
#   pass

# my_function()


# Recursion : calling a function inside itself or calling a function with in the same function


# def my_function():
#   print("Hello")

#   my_function()

# my_function()

# 1 : base condition
# 2. Function should have parameters + return

# Some of the first n natural numbers using recursion.

# def my_function(n):

#   if n == 0:
#     return 0

#   return  my_function(n-1) + n


# n1 = int(input('Enter n value: '))

# answer = my_function(n1)

# print(answer)

# Write a function to find sum  of the digits of a number using recursion.


# def sum_of_digits(n):
#   # base case : if n is 0, return 0
#   if n == 0:
#     return 0

#   else :
#     # Recursive case: last digit of n  + sum of remaining digits
#     return n % 10 + sum_of_digits(n // 10)
#   # 5 + sum_of_digits(1234)
#   # 4 + sum_of_digits(123)
#   # 3 + sum_of_digits(12)
#   # 2 + sum_of_digits(1)
#   # 1 + sum_of_digits(0) = sum_of_digits(1) = 1
#   # 0

# print(sum_of_digits(12345))

# What is Palindrome?
# A palindrome is word , pharse , or number, or sequence of charaters that reads the same backward as forward.

# radar
# madam
# level


# 2. Pharses:
# A man a plan, a canal,  Panama

# No lemon, no melon

# Numbers
# 121
# 12321
# 4554
# 4565456


# def is_palindrome(s):
#   # base case : if string has 0 or 1 characters, its a palindrome
#   if len(s) <= 1:
#     return True
#   # recursive case
#   return s[0] == s[-1] and is_palindrome(s[1:-1])

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))

# list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(list[1:-1])


def is_palindrome(s):
    # base case : if string has 0 or 1 characters, its a palindrome
    if len(s) <= 1:
        return True
    # recursive case
    return s[0] == s[-1] and is_palindrome(s[1:-1])


print(is_palindrome("racecar"))



