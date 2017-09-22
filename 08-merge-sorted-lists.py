# Author: Keith Williams
# Date: 22/09/2017
# Adapted from:
#	https://stackoverflow.com/questions/4173225/my-implementation-of-merging-two-sorted-lists-in-linear-time-what-could-be-imp
#	https://docs.python.org/3/library/functions.html#sorted

from sys import argv

# THIS FUNCTION DEMONSTRATES HOW TO MERGE AND SORT TWO LISTS WITH THE BUILT-IN SORT FUNCTION.
# This is function takes two lists, sorted or unsorted, as arguments.
# It is responsible for merging these lists into a single sorted list.
# First the lists are concatenated together to form a new list.
# This function uses the built-in sorted method to sort this new list.
# Note that this function can return a list with duplicate elements.
def merge_lists(l1, l2):
	return sorted(l1 + l2)

# THIS FUNCTION DEMONSTRATES AN ALGORITHM FOR MERGING AND SORTING TWO SORTED LISTS.
# This is function takes two sorted lists as arguments.
# It is responsible for merging these lists into a single sorted list.
# First a new list is created and will be used to store the sorted elements.
# A while loop continues to loop one of the sorted lists are empty
# In this loop the first element of both sorted lists are compared.
# If the first emelent in the first sorted list is the smallest it is appended to the new sorted list and popped off.
# Otherwise the first emelent in the second sorted list appended to the new sorted list and popped off, even if the two elements are equal.
# When this loop ends there will be at least one element remaining in one of the sorted lists.
# Therefore, the two sorted lists, one of which will always be empty, are concatenated to the new list before being returned.
# Note that this function can return a list with duplicate elements.
def merge_sorted_lists(l1, l2):
	l = []
	
	while l1 and l2:
		if l1[0] < l2[0]:
			l.append(l1.pop(0))
		else:
			l.append(l2.pop(0))
	
	return l + l1 + l2

# This function parses the nth argument to a list of integers.
# 1) First get the first command line argument as a string - argv[n]
# 2) Break this comma separated string up into a list of substrings - .split(',')
# 3) Using the built-in map function apply the built-in int function to each element of the substring.
#    This will convert each element to an int, if possible, and return the new list of ints.
#    If any of the strings cannot be parsed to an int then a message is outputted to inform the user and None is returned.
def get_integer_list(n):
	try:
		return map(int, argv[n].split(','))
	except ValueError:
		print("(%s) Invalid argument!" % (n))
	except IndexError:
		print("No argument at (%s)!" % (n))

# Only execute this function if this is the main module.
# Parse the first two command line arguments to a lists of integers and print the combined merged list.
if __name__ == "__main__":
	l1 = get_integer_list(1)
	l2 = get_integer_list(2)
	
	if l1 and l2:
		print(merge_sorted_lists(l1, l2))