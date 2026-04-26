import random
from art import logo

number = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# print(number)
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level == "easy":
    attempts = 10
else:
    attempts = 5
print(f"You have {attempts} remaining to guess the number.")
while attempts > 0:
    guess = int(input("Make a guess : "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess>number:
        print("Too high.")
    else:
        print("Too low.")
    attempts -=1
    if attempts == 0:
        print("You've run out of guesses. You lose.")
    else:
        print("Guess again.")
        print(f"You have {attempts} remaining to guess the number.")
