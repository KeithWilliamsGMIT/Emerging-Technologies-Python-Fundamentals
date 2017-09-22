# Author: Keith Williams
# Date: 21/09/2017

from sys import argv
import math

# This script takes one command line argument to calculate the factorial digit sum for.
# If the argument is not a number, print "Invalid argument!".
# There are two steps in calculating the factorial digit sum of a number.
# 1) Calculate the factorial
#	In this case the factorial is calulated using the factorial function from the math library which was imported above.
# 2) Calculate the digit sum
#	A) Convert the result of the factorial function to a string, which is iterable - str(factorial)
#	B) This is passed as the second argument to the built-in map function and the built in int function is passed as the first.
#	   This map method will pass each character of the string to the int function, returning a list of ints - map(int, str(factorial))
#	C) Finally this list of ints are passed to the built-in sum function which sums each element in the list - sum(map(int, str(factorial)))

# Read the first command line argument
arg = argv[1]

try:
    # Try to convert to an int
    n = int(arg)
    
    # Calculate the factorial of the number
    factorial = math.factorial(n)
    
    # Calculate the sum of it's digits
    digit_sum = sum(map(int, str(factorial)))
    
    # Print the result
    print(digit_sum)
except ValueError:
    print("Invalid argument!")