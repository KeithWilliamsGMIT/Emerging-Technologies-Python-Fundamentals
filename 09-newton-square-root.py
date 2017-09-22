# Author: Keith Williams
# Date: 22/09/2017

from sys import argv
from math import sqrt

# This function is responsible for approximating the square root of a number using Newton's method.
# This function takes one argument, ideally a float, for which to approximate the square root for.
# First a starting point, z, is calculated by dividing the original number by two.
# Apply z - ((z*z - x) / (2 * z)) ten times to approximate the square root of x.
def newton_square_root(x):
	current = x / 2
	
	for i in range(10):
		current = z_next(x, current)
	
	return current

# This function is responsible for evaluating z - ((z*z - x) / (2 * z)) where:
#   A) x is the original number.
#   B) z is the starting/current number.
# These values, ideally floats, are passed in as arguments to the function.
# This value is then returned.
def z_next(x, z):
	return (z - ((z * z - x) / (2 * z)))

# Only execute this function if this is the main module.
# Parse the first command line argument to a float if possible.
# Then output the square root of that number, calculated using newton's method and the math.sqrt() function.
# Otherwise, output an error message.
if __name__ == "__main__":
	try:
		number =  float(argv[1])
		
		if number is not None and number > 0:
			print("newton_square_root(%f) = %f" % (number, newton_square_root(number)))
			print("match.sqrt(%f) = %f" % (number, sqrt(number)))
		else:
			print("Invalid number! Must be a positive number greater than zero!")
	except ValueError:
		print("(%s) Invalid argument!" % (n))
	except IndexError:
		print("No argument!")