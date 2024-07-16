# calculator 

def add(n1, n2 ):
  return n1 + n2


# Subtract

def Subtract(n1, n2 ):
  return n1 - n2

# Multiplying


def multiply(n1, n2 ):
  return n1 * n2


# Divide 


def divide(n1, n2 ):
  return n1 / n2




operations = {
  "+": add,
  "-": Subtract,
  "*": multiply,
  "/": divide
}


num1 = float(input("What's the first number?: "))
num2 = float(input("What's the second number?: "))

# loop through the dictionary(operations)

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")