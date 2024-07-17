# Variables are dynamicly typed
# n = 0
# print('n =', n)
# # >>> n = 0

# n = "abc"
# print('n =', n)

# n = 4
# n = None
# print("n =", n)

# for i in range(2, 6):
#     print(i)

# Looping from i = 5 to i = 2
# for i in range(5, 1, -1):
#     print(i)

# # Division is decimal by default
# print(5 / 2)

# # Double slash rounds down
# print(5 // 2)


# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
# print(-3 // 2)

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
# print(int(-3 / 2))
# print(-3//2)


# #Modding is similar to most languages
# print(10 % 3)

# # Except for negative values
# print(-10 % 3)

# # Arrays (called lists in python)
# arr = [1, 2, 3]
# print(arr)

# Can be used as a stack
# arr.append(4)
# arr.append(5)
# print(arr)
# arr.pop()
# print(arr)
# arr.insert(1, 7)
# print(arr)
# arr[0] = 0
# arr[3] = 0
# print(arr)
# # Initialize arr of size n with default value of 1
# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))
# arr = [1, 2, 3, 4]

# print(arr[0:5])

# a, b, c = [1, 2, 3]
# print(a, b, c)


# # Be careful though
# a, b = [1, 2, 3]
# print(a, b)

# # Loop through arrays
# nums = [1, 2, 3]

# # Using index
# for i in range(len(nums)):
#     print(nums[i])


# nums1 = [1, 2, 3]

# for k in range(nums1):
#     print(k)

# for n in nums:
#     print(n)

# Variables are dynamicly typed
# n = 0
# print('n =', n)
# # >>> n = 0

# n = "abc"
# print('n =', n)
# # >>> n = abc

# # Multiple assignments
# n, m = 0, "abc"
# n, m, z = 0.125, "abc", False

# Increment
# n = n + 1 # good
# n += 1    # good
# n++       # bad

# None is null (absence of value)
# n = 4
# n = None
# print("n =", n)
# >>> n = None


# If statements don't need parentheses 
# or curly braces.
# n = 1
# if n > 2:
#     n -= 1
# elif n == 2:
#     n *= 2
# else:
#     n += 2

# Parentheses needed for multi-line conditions.
# # and = &&
# # or  = ||
# n, m = 1, 2
# if ((n > 2 and 
#     n != m) or n == m):
#     n += 1


# n = 5
# while n < 5:
#     print(n)
#     n += 1

# # Looping from i = 0 to i = 4
# for i in range(5):
#     print(i)

# # Looping from i = 2 to i = 5
# for i in range(2, 6):
#     print(i)

# # Looping from i = 5 to i = 2
# for i in range(2, 25, 2):
#     print(i)


# # Division is decimal by default
# print(5 / 2)

# # Double slash rounds down
# print(-5 // 2)

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
# print(-7 // 2)

# # A workaround for rounding towards zero
# # is to use decimal division and then convert to int.
# print(int(-3 // 2))


# # Modding is similar to most languages
# print(10 % 3)

# # Except for negative values
# print(-10 % 3)

# print(-29 % 3)


