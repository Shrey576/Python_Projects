import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    is_guessed = False  # Boolean to track if the number is guessed

    print("Guess the number between 1 and 100!")

    while not is_guessed:
        guess = int(input("Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number!")
            is_guessed = True  # Change the boolean to True once guessed

guess_number()
