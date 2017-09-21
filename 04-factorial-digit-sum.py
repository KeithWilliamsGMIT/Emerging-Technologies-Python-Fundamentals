# Author: Keith Williams
# Date: 21/09/2017

from sys import argv
import math

# Read the first command line argument
arg = argv[1]

# Try to convert to an int
n = int(arg)

# Calculate the factorial of the number
factorial = math.factorial(n)

# Calculate the sum of it's digits
digit_sum = sum(map(int, str(factorial)))

# Print the result
print(digit_sum)