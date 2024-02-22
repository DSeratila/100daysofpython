#number guessing game
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')


def compare(number_to_guess, user_guess):
    if number_to_guess == user_guess:
        return "="
    elif number_to_guess < user_guess:
        return ">"
    else:
        return "<"


difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
attempts = 0
number_to_guess = random.randint(1, 100)
print(str(number_to_guess) + "<-----")
won = False

if difficulty == 'easy':
    attempts = EASY_LEVEL_ATTEMPTS
elif difficulty == 'hard':
    attempts = HARD_LEVEL_ATTEMPTS



while attempts > 0 and not won:
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess: "))
    comparison_result = compare(number_to_guess, guess)

    if comparison_result == "=":
        won = True
    elif comparison_result == ">":
        print("Too high.")
    else:
        print("Too low.")

    if attempts > 0 and not won:
        print("Guess again.")

    attempts -= 1

if won:
    print(f"You got it! The answer was {number_to_guess}.")
else:
    print("You've run out of guesses, you lose.")