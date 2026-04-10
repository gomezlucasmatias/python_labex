import random

# Generate random number between 1 and 100
number = random.randint(1, 100)
attempts = 0

# The game starts
print("Guess the number that I thinking of between 1 and 100")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct 🎉")
        print("Attempts:", attempts)
        break

