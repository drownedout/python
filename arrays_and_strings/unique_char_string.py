# The following algorithms will determine if all characters in a string are unique.

# Assumptions: 
	# - ASCII characters
	# - Case sensative - capital and lowercase letters are considered
	#	unique characters. Example: 'a' != 'A'


class UniqueCharacters(object):

	# Methods of solving this problem

	def length(self, string):
		# If none, return false
		if string is None:
			return False
		# Will return true if the set() and length are the same
		# set() only stores one instance of a value, so if the lengths
		# are the same, then all the characters must be unique
		return len(set(string)) == len(string)


	def hash_map(self, string):
		# If none, return false
		if string is None:
			return False
		# Using set() to store unique characters
		character_set = set()
		for char in string:
			if char in character_set:
				# if the character is in character_set, return False
				return False
			else:
				# else, add character to character_set
				character_set.add(char)
		return True


	def scan(self, string):
		# If none, return false
		if string is None:
			return False
		for char in string:
			# Iterates through each character in the string, and scans
			# to see if the character appears more than once in a string
			if string.count(char) > 1:
				return False
		return True

# Testing the code

unique_test = UniqueCharacters()

unique_test.length("Hobbit") # False
unique_test.length("Zebra") # False

unique_test.hash_map("Hobbit") # False
unique_test.hash_map("Zebra") # False

unique_test.scan("Hobbit") # False
unique_test.scan("Zebra") # False