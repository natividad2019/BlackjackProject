import os

def clear():
    # Clear the screen using the appropriate command based on the operating system
    os.system('clear')

def add(n1, n2):
    print(f"Adding {n1} and {n2}")  # Debugging
    return n1 + n2

def subtract(n1, n2):
    print(f"Subtracting {n2} from {n1}")  # Debugging
    return n1 - n2

def multiply(n1, n2):
    print(f"Multiplying {n1} and {n2}")  # Debugging
    return n1 * n2

def divide(n1, n2):
    print(f"Dividing {n1} by {n2}")  # Debugging
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()  # Clearing the screen initially
  
    # Asking the user to input the first number.
    num1 = float(input("What's the first number?: "))
    print(f"First number: {num1}")  # Debugging
  
    # Printing the operation symbols (+, -, *, /) for the user to see.
    for symbol in operations:
        print(symbol)
  
    # A flag to keep the calculator running.
    should_continue = True

    while should_continue:  # Start of the while loop
        # Asking the user to pick an operation.
        operation_symbol = input("Pick an operation: ")
        print(f"Chosen operation: {operation_symbol}")  # Debugging
    
        # Asking the user for the next number.
        num2 = float(input("What's the next number?: "))
        print(f"Next number: {num2}")  # Debugging
    
        # Getting the function from the operations dictionary.
        calculation_function = operations[operation_symbol]
        print(f"Calculation function: {calculation_function}")  # Debugging
    
        # Calling the function with num1 and num2 as arguments and storing the result in answer.
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")  # Debugging

        # Asking if the user wants to continue with the current result or start a new calculation.
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer  # Updating num1 to the current answer to continue calculations.
            print(f"Continuing with new num1: {num1}")  # Debugging
        else:
            should_continue = False  # Setting the flag to False to stop the while loop.
            clear()  # Clearing the screen
            calculator()  # Restarting the calculator function for a new calculation.

# Starting the calculator.
calculator()
