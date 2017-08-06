# The following algorithms will determine whether or not a string is 
# a permutation of another string.

# Assumptions
	# The string is ASCII
	# Whitespace is included
	# It is case sensative
	# Will return True or False

# Importing defaultdict class from collections for hash_permutation.
# For more information on defaultdict(), you can read the documentation linked below:
# https://docs.python.org/2/library/collections.html
from collections import defaultdict

class Permutation(object):

	def sorted(self, str1, str2):
		if str1 is None or str2 is None:
			return False

		# Sorts the strings to see if they return the same value
		# Can be slow if user inputs large strings
		return sorted(str1) == sorted(str2)

	def hash_permutation(self, str1, str2):
		if str1 is None or str2 is None:
			return False
		# Checks to see if the length of the strings are equal
		# If they are a permutation of each other, they should
		# be the same length
		if len(str1) != len(str2):
			return False

		# defaultdict() is a built-in subclass of dict()
		# Setting the default_factory to 'int' is useful for counting
		# The keys placed into the dictionaries below will default to a value of 0.
		unique_char_count1 = defaultdict(int)
		unique_char_count2 = defaultdict(int)

		# Sets for loops for each string.
		# Char is the key and the the 'int' is the value inside
		# the unique_char_count dictionary
		for char in str1:
			unique_char_count1[char] += 1
		for char in str2:
			unique_char_count2[char] += 1

		# Compares the two dictionaries to see if they are the same
		return unique_char_count1 == unique_char_count2




permutation_test = Permutation()

permutation_test.sorted("bears, beats, battlestar", "beats bears,, battlestar" ) # True
permutation_test.hash_permutation("bears, beats, battlestar", "beats bears,, battlestar" )) # True

permutation_test.sorted("bears, beats, battlestar", "beats bears,, ar" ) # False
permutation_test.hash_permutation("bears, beats, ", "beats bears,, battlestar" ) # False
