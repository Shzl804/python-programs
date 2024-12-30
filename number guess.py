import random

def user_guesses_number():
    print("Welcome to the Number Guessing Game!")
    print("I have thought of a number between 1 and 100. Can you guess it?")
    
    # The computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    tries = 0
    
    while True:
        tries += 1
        # The user makes a guess
        guess = int(input("Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {tries} tries.")
            break

# Start the game
user_guesses_number()






















