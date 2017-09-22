# Author: Keith Williams
# Date 22/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/509211/explain-slice-notation

from sys import argv

# This function takes one argument which is the value to check is a palindrome.
# This value is converted to a string so it does not initially need to be one.
# The spaces are removed and all characters are converted to lowercase.
# For example, the value "Nurses Run" is converted to "nursesrun".
# The resulting string is then reversed using [::-1] and compared to the original.
# This is called slicing and has the optional arguments [start:end:step].
#	A) start: The beginning index of the slice, it will include the element at this index unless it is the same as stop, defaults to 0, i.e. the first index. If it's negative, it means to start n items from the end.
#	B) stop: The ending index of the slice, it does not include the element at this index, defaults to length of the sequence being sliced, that is, up to and including the end.
#	C) step: The amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.
# By leaving the start and stop as the default values and setting the step value to -1 it reverses the string.
# This function returns true is the string is a palindrome, ottherwise it returns false.
def palindrome(phrase):
	chars = str(phrase).replace(' ', '').lower()
	
	return chars == chars[::-1]

# Only execute this function if this is the man module.
# Read the first command line argument and pass check if it is palindrome.
# Output "True" if it is. Otherwise, output "False".
if __name__ == "__main__":
	try:
		print(palindrome(argv[1]))
	except IndexError:
		print("No argument!")