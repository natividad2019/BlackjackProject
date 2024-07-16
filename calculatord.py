import os

def clear():
    print("\n" * 100)

# calculator

# addition
def add(n1, n2):
    return n1 + n2

# subtraction


def subtract(n1, n2):
    return n1 - n2

# multiplication


def multiply(n1, n2):
    return n1 * n2
    

# division


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

    

# Get user input for the first number

num1 = int(input("What's the first number?: "))
print(f"First number: {num1}")
# Get the user input for the second number
num2 = int(input("What's the second number?: "))
print(f"Second number: {num2}")


# Loop to display available operations


for symbol in operations:
    print(symbol)



should_continue = True

while should_continue:

# Get  user input for the operation
  operation_symbol = input("Pick an operation from the line above: ")
  print(f"Operation Selected: {operation_symbol}")


  # find the function corresponding to the chosen operation

  calculation_function = operations[operation_symbol]
  print(f"Calculation function: {calculation_function}")

  #  Perform the calculation
  answer = calculation_function(num1, num2)


  print(f"{num1} {operation_symbol} {num2} = {answer}")


  # Asking if the user wants to continue with the current result or start  a new calculator 
  if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
    num1 = answer
  else:
    should_continue = False # setting the flag to false to stop the while loop
    clear() # Clear the screen 


