# Function with inputs 

# def my_function():
  # #Do this 
  # # then do this 
  # # finally do this\
  # pass

#Review : 
# Create a function called greet().
# Write 3 print statements inside the function.
# # Call the greet() function and run your code.
# def greet():
#   print("Hello there")
#   print("How are you do Vamsi?")
#   print("Isn't the weather nice today?")

# greet()

# functions with  inputs
# def my_function(something):
#Do this  somthing 
# then do this 
# finally do this\
# pass

# def greet_with_name(name):
#   print(f"Hello {name}")
#   print(f"How are you doing {name}?")

# greet_with_name("Vinny")
# # name = Parament 
# Vinny = Argument

# functions with  more than 1 input 

# def greet_with(name, location):
#   print(f"Hello {name}")
#   print(f"What is it like in {location}?")
#   print("I am doing fine today")
#   # functions with keyword arguments
# greet_with(name = "Vinny", location = "Canada")

'''
Postional Arguments
def my_function(a, b, c):
#Do this  a 
# then do this wiht b
# finally do this with c
# pass

'''

'''

Keyword Arguments

def my_function(a, b, c):
#Do this  a 
# then do this wiht b
# finally do this with c
# pass
'''
'''
You are paointing a wall. The instructions on paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint = test_h * test_w / coverage
num_cans = paint
print(f"You'll need {num_cans} cans of paint.") 

'''

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint = test_h * test_w / coverage
# num_cans = paint
# print(f"You'll need {num_cans} cans of paint.") 

import math
def paint_calc(height, width, cover):
  area = height * width
  num_cans = area / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {num_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)