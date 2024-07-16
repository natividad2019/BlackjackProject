# Creating a dictionary
# student = {
#     "name": "James",
#     "student_id": 1245,
#     "feedback": None,
#     "age": 18,
#     "grade": "11th"

# }

# print(student)

# Access values  using key
# print(student["name"])
# print(student["student_id"])

# Adding or updating key - value pairs

# # Add a new key value pair
# student["school"] = "Universiry of Utah"

# # update an existing key value pair
# student["grade"] = "12th"

# print(student)

# Add new key value pair

# Removeing Key - Value Pairs
# You can remove key -value pairs  using the del keyword or pop () method
# del student["age"]
# student.pop("grade")

# print(student)


# Loop through keys
# for key in student:
#   print(key)


# Loop through values
# for value in student.values():
#   print(value)


# Loop through key value pairs
# for key, value in student.items():
#   print(f"{key} : {value}")

# check if a key exits
# if "name" in student:
#   print("Name is present is the dictionary")

# if "age" not in student:
#   print("Age is not present in the dictionary")
# else :
#   print("Age is present in the dictionary")

# grades = {
#     "Vinodh": 96,
#     "Srikanth": 87,
#     "Vamsi": 90,
#     "David": 85,
#     "Naveen": 88
# }

# # calculate the average grade 
# total = 0
# for grade in grades.values():
#   total = total + grade
#   average = total / len(grades)

# print(f"Average grade is {average}")


# # create a empty dictionary to store student grades 
# grades = {}

# # step 2 : Ask the user for the number of students 
# num_students = int(input("Enter the number of students: "))

# # step 3 : loop through the number of students 
# for _ in range(num_students):
#   name = input("Enter the name of the student: ")
#   grade = int(input("Enter the grade of the student: "))
#   grades[name] = grade

# # step 4 : Initialize a varible to hold the sum of all grades 
# total = 0

# # step 5 : Loop through the dictionary to sum all the grades 
# for grade in grades.values():
#   total += grade  
#   print(f"Added {grade}. Total is now {total}") # Debugging statement


# # step 6 : Calculate the average grade

# average = total / len(grades)
# print(f"Average grade is {average}")


# # step 7 : Print each students grade 
# print("\nIndividual student grades:")

# for student, grade in grades.items():
#   print(f"{student}: {grade}")

  # Nesting a dictionary in a dictionary 

# capitals = {
#      "France": "Paris",
#      "Germany": "Berlin"
#  }

# # Nesting a List in a Dictionary
# travel_log = {
#      "France": ["Paris", "Lille", "Dijon"],
#      "Germany": ["Berlin", "Hamburg", "Stuttgart"]
#  }

# print(travel_log["France"][0])

#nesting a dictionary in a list and a dictionary

#{ key :[list], key2: {dict} }

# capitals = {
#      "France": "Paris",
#      "Germany": "Berlin"
#  }

# Nesting a list a dictionary

# travel_log =  {
#  "France": "Paris", "Little, "Dijon",
# }

# travel_log = {
#   "France" : ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# Nesting Dictionary in a Dictionary

# travel_log = {
#   "France" : {"cities_visited": ["Paris", "Lttle", "Dijon"]},
#   "Germany" :{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
# }

# Nesting Dictionary in a List


# travel_log = [
#   {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#   },
#   {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#   },
# ]

# print(travel_log[1]["total_visits"])

# def my_function(n, m):
#   result = 1 + 11
#   return result

# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You did not provide valid inputs"
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"{formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), 
#                   input("What is your last name? ")))

# vin = '''
# hitheheheireir=-0987rdvbnjkjhgfvcbkhgfvbnjkjuhgvbnjkhg'''


# print(vin)

# Doctstings for Modules 
# A module-level dscstring appears at the top of a Python file and describes the purpose and content of the module.
# '''

# this module provides utlilites for mathmatical operations'''

# import math

class Calculator:
  '''
  This class provides utlilites for mathmatical operations'''
  pass
  # def __init__(self, x, y):
  #   self.x = x
  #   self.y = y

  # def add(self):
  #   return self.x + self.y

  # def sub(self):
  #   return self.x - self.y
