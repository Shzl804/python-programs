

import random

# Calculator Function
def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    # Main calculator logic
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

# Even or Odd Function
def even_or_odd():
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        print(f"{a} entered number is even")
    else:
        print(f"{a} entered number is odd")

# Factorial Function
def factorial():
    def find_factorial(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * find_factorial(n - 1)

    fact = int(input("Enter a number that you want to find factorial: "))
    print(f"The factorial of {fact} is {find_factorial(fact)}")

# Liar Detector Function
def liar_detector():
    def detect_word(answer):
        if answer.isdigit():
            return "This is not your name, and you are a liar."
        elif answer.isalpha():
            return "Good! Your name seems valid."
        else:
            return "You are a liar."

    # Function to ask random questions and detect lies in the answers
    def ask_question():
        questions = [
            "Did you do your homework?",
            "Have you ever lied to your friend?",
            "Do you really like Pathaan movie?"
        ]
        question = random.choice(questions)
        print(question)

    a = input("Hello! My name is Shahzeel. Tell me your name: ")

    # Check if the input is a valid name
    result = detect_word(a)
    print(result)

    # If the name is valid (i.e., only alphabetic), ask questions
    if a.isalpha():
        print(f"Hi {a}! Can I ask you some questions? If yes, enter 'yes'.")
        b = input("Are you ready? (yes/no): ").strip().lower()

        if b == 'yes':
            # Ask the question and detect lies in the answer
            ask_question()
            answer = input("Your answer: ")
            lie_result = detect_word(answer)
            print(lie_result)
        else:
            print("Okay, maybe next time!")
    else:
        print("Please enter a valid name using only alphabetic characters.")

# Main Program Loop
def main():
    while True:
        print("\nThis is my all-in-one program.\nIn this program, I have added:")
        print("1. Calculator (1)")
        print("2. Even or Odd (2)")
        print("3. Factorial (3)")
        print("4. Liar Detector (4)")

        a = input("Press (1/2/3/4) to choose an option or type 'exit' to quit: ")

        if a == "1":
            calculator()
        elif a == "2":
            even_or_odd()
        elif a == "3":
            factorial()
        elif a == "4":
            liar_detector()
        elif a.lower() == "exit":
            print("Thank you for using the program! Goodbye.")
            break
        else:
            print("Invalid choice! Please press (1/2/3/4) or type 'exit'.")

        # Ask the user if they want to continue or exit
        continue_choice = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the program! Goodbye.")
            break

# Start the program
if __name__ == "__main__":
    main()
