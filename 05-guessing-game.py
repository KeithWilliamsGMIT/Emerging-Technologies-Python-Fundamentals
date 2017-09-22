# Author: Keith Williams
# Date 22/09/2017
# Adapted from:
#	http://pythoncentral.io/how-to-generate-a-random-number-in-python/
#	http://sweetme.at/2014/01/22/how-to-get-user-input-from-the-command-line-in-a-python-script/

from random import randint

# This is the main function that's responsible for defining the game logic.
# The steps can be broken down into the following steps:
# 1) Generate a random number between 1 and 100 which will be the secret the user must try to guess.
#   This will be achieved using the randint function from the random library, which is imported above.
# 2) The next step is to get the user input from the console.
# 3) If that guess was already made print a message informing the user.
# 4) Otherwise do the following:
#	1) Add that guess to a list of guesses.
#	2) Increment the number of tries by one.
#	3) Inform the user if the guess was either too high or too low.
# 5) Once the user successfully guesses the secret, print the number of tries and all the guesses the user made.
def play_game():
	# Choose random number between 1 and 100 to be the secret
	secret = randint(1, 101)
	
	tries = guess = 0
	guesses = []
	
	# Loop while the user has not guessed the secret
	while guess is not secret:
		guess = get_user_input()
		
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

# This function is responsible for prompting the user for a number input, or a guess.
# If the input is a valid integer between 1 and 100 then that number is returend.
# Otherwise an error meesage is outputted to the console and None is returned.
def get_user_input():
	user_input = input("Guess the number: ")
    
	try:
		number = int(user_input)
        
		if number >= 1 and number <= 100:
			return number
		else:
			print(str(number) + " must be between 1 and 100!")
	except ValueError:
		print(user_input + " is not a valid input!")

# Only start the game if this is the main module.
if __name__ == "__main__":
	play_game()