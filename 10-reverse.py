# Author: Keith Williams
# Date: 22/09/2017

from sys import argv

# This function takes one argument which is the value to reverse.
# This value is converted to a string so it does not initially need to be one.
# The string is then reversed using [::-1].
# This is called slicing and has the optional arguments [start:end:step].
#	A) start: The beginning index of the slice, it will include the element at this index unless it is the same as stop, defaults to 0, i.e. the first index. If it's negative, it means to start n items from the end.
#	B) stop: The ending index of the slice, it does not include the element at this index, defaults to length of the sequence being sliced, that is, up to and including the end.
#	C) step: The amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.
# By leaving the start and stop as the default values and setting the step value to -1 it reverses the string.
def reverse(string):
    return str(string)[::-1]

# Only execute this function if this is the main module.
# Parse the first command line argument as a string if there is one.
# Reverse this string and return the result.
# If there is no argument output a message.
if __name__ == "__main__":
	try:
		print(reverse(argv[1]))
	except IndexError:
		print("No argument!")