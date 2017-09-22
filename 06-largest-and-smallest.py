# Author: Keith Williams
# Date 22/09/2017
# Adapted from:
#	https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08

from sys import argv

# THIS FUNCTION DEMONSTRATES AN ALGORITHM TO RETURN THE LASRGEST AND SMALLEST VALUES IN A LIST.
# This function takes a list as a parameter.
# The largest and smallest values are set to the first element in the list.
# All elements are then iterated over and compared to the largest, and possibly smallest, values.
# If the new element is larger than the current largest it becomes the new largest and likewise for the smallest.
# These values are returned as a tuple which can be unpacked by the calling function.
# Note that the fist value in the tuple is the largest and the second value is the smallest.
def get_largest_and_smallest_manually(l):
	largest = smallest = l[0]
	
	for i in l:
		if l[i] > largest:
			largest = l[i]
		elif l[i] < smallest:
			smallest = l[i]
	
	return largest, smallest

# THIS FUNCTION DEMONSTRATES HOW TO RETURN THE LASRGEST AND SMALLEST VALUES IN A LIST USING THE BUILT-IN MAX AND MIN FUNCTIONS.
# This function takes a list as a parameter.
# It uses the built-in max and min functions to find the largest and smallest values in the list.
# These values are returned as a tuple which can be unpacked by the calling function.
# Note that the fist value in the tuple is the largest and the second value is the smallest.
def get_largest_and_smallest(l):
	return max(l), min(l)

# Only execute this function if this is the main module.
# This function parses the first argument to a list of integers.
# 1) First get the first command line argument as a string - argv[1]
# 2) Break this comma separated string up into a list of substrings - .split(',')
# 3) Using the built-in map function apply the built-in int function to each element of the substring.
#    This will convert each element to an int, if possible, and return the new list of ints.
#    If any of the strings cannot be parsed to an int then a message is outputted to inform the user and None is returned.
# If the argument is structured correctly pass the list to a function to find the largest and smallest values and output the result.
if __name__ == "__main__":
	try:
		l = map(int, argv[1].split(','))
		largest, smallest = get_largest_and_smallest_manually(l)
		print("Smallest: " + str(smallest))
		print("Largest: " + str(largest))
	except ValueError:
		print("Invalid argument!")