# Author: Keith Williams
# Date 22/09/2017
# Adapted from:
#	http://pythoncentral.io/how-to-generate-a-random-number-in-python/

from random import randint

# Choose random number between 1 and 100 to be the secret
secret = randint(1, 101)

tries = guess = 0
guesses = []

# Loop while the user has not guessed the secret
while guess is not secret:
    guess = input("Guess the number: ")

    if guess in guesses:
        print("You've already guessed " + str(guess))
    elif guess is not None:
        guesses.append(guess)
        tries += 1

        # Print if the guess is too high or to low
        if guess > secret:
            print("Too High")
        elif guess < secret:
            print("Too Low")

print("You win!")
print("Tries: " + str(tries))
print("Guesses: " + str(guesses))