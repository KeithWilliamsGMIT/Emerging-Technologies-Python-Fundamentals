# Author: Keith Williams
# Date: 21/09/2017

# This script iterates between the numbers 1 and 100.
# For each iteration there is a condition for each of the following:
# 1) For numbers which are multiples of both three and five print "FizzBuzz".
# 2) For multiples of three print "Fizz".
# 3) For multiples of five print "Buzz".
# 4) Otherwise print the number.
for i in range(1, 101):
	if i%3 == 0 and i%5 == 0:
		print("FizzBuzz")
	elif i%3 == 0:
		print("Fizz")
	elif i%5 == 0:
		print("Buzz")
	else:
		print(i)