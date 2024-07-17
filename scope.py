# principal = "MR Vinny"  # Global varaible
# # The principal is a global variable, known by everyone
# # Each teacher is a local variable, only known inside their respective classroom(function)

# def classroom1():
#   teacher = "Mr. Mason"  # Local variable
#   print(f"The teacher in Classroom 1 is {teacher}")
#   print(f"Principal in Classroom 1 is {principal}")


# def classroom2():
#   teacher = "Mr. Landon"  # Local variable
#   print(f"The teacher in Classroom 2 is {teacher}")
#   print(f"Principal in Classroom 2 is {principal}")


# classroom1()
# classroom2()



# print(f"The principal in Classroom 1 is {principal}")

# Block Scope

# if True:
#   block_variable = "I am inside an if block"
#   print(block_variable) # This will work and print the value

#   # Modifying a Gloabl varaible 

#   # To modify a global variable, you need to use the global keyword

#   counter = 0 # Global variable
#   def increase_counter():
#     global counter

#     counter  = counter + 1
#   increase_counter()
#   print(counter)


# MAX_STUDENTS = 30 # Global variable


# def enroll_student(current_students):
#     if current_students < MAX_STUDENTS:
#        current_students = current_students +1
#        print(f"Students enrolled successfully {current_students}" )
#     else:
#        print("Class is full")
#     return current_students
  

#   # current_students = 28
# presnt_students = enroll_student(28)
# # print(presnt_students)