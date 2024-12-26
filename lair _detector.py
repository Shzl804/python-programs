import random

# Function to detect whether the input is a number, name, or invalid input
def detect_word(a):
    if a.isdigit():
        return "This is not your name, and you are a liar."
    elif a.isalpha():
        return "Good! Your name seems valid."
    else:
        return "You are a liar."

# Function to ask random questions and detect lies in the answers
def ask_question():
    questions = [
        "Did you do your homework?",
        "Have you ever lied to your friend?",
        "Do you really like this movie?"
    ]
    
    # Choose a random question from the list
    question = random.choice(questions)
    
    # Ask the user the question
    print(question)
    answer = input("Your answer: ")
    
    # Detect if the answer might be a lie based on certain words
    return detect_word(answer)

# Main program
a = input("Hello! My name is Shahzeel. Tell me your name: ")

# Check if the input is a valid name
result = detect_word(a)
print(result)

# If the name is valid (i.e., only alphabetic), ask questions
if a.isalpha():
    print(f"Hi {a}! Can I ask you some questions? If yes, then enter 'yes'.")
    b = input("Are you ready? (yes/no): ").strip().lower()
    
    if b == 'yes':
        # Ask the question and detect lies in the answer
        lie_result = ask_question()
        print(lie_result)
    else:
        print("Okay, maybe next time!")
else:
    print("Please enter a valid name using only alphabetic characters.")

