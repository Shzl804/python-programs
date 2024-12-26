# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program
print("This is my first calculator.\n")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input for operation choice
c = input("Enter operand number (1/2/3/4): ")

# Get user input for the numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Perform the operation based on the user's choice
if c == '1':
    print(f"{a} + {b} = {add(a, b)}")
elif c == '2':
    print(f"{a} - {b} = {subtract(a, b)}")
elif c == '3':
    print(f"{a} * {b} = {multiply(a, b)}")
elif c == '4':
    print(f"{a} / {b} = {divide(a, b)}")
else:
    print("Something went wrong! Please choose a valid operation (1/2/3/4).")
   


