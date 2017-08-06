# The following algorithms will compress a string, leaving only unique characters 
# and the character count.
# However, this will only run if it saves space.
# For example, 'AABBCC' would remain 'AABBCC' but 'AAABBCC'
# would become 'A3BBCC'

# Assumptions: 
	# - ASCII characters
	# - Case sensative - capital and lowercase letters are considered
	#	unique characters. Example: 'a' != 'A'

class CompressString(object):

	def compress(self, string):
		# Checks if string is empty
		if string is None or not string:
			return string

		# Set result to empty string
		result = ''

		# Initializes previous_char to first character of the string
		previous_char = string[0]

		# Set counter to 0
		count = 0

		# Iterate through each character in string
		for char in string:
			# If the current character is the same as the previous character,
			# count is incremented by 1
			if char == previous_char:
				count += 1
			# Else, _calculate_partial_result is called, concatenating the previous character
			# and its count to result.
			else:
				# Concats the result of '_calculate_partial_result'
				result += self._calculate_partial_result(previous_char, count)
				# Previous char is now set to the current char
				previous_char = char
				# Count is reset to 1
				count = 1
		# Catches the last instance of a character and concats it to result since it wouldn't
		# be caught in the else statement above
		result += self._calculate_partial_result(previous_char, count)

		# Returns the result if it's shorter than initial string
		return result if len(result) < len(string) else string


	# A private helper method for the 'compress' function
	# Returns the previous character and its count if it's greater than one.
	# Otherwise, if the count is less than one, it will just return the previous character
	def _calculate_partial_result(self, previous_char, count):
		return previous_char + (str(count) if count > 1 else '')

compress_test = CompressString()

compress_test.compress('AAAABBBCCCDEEE') #A4B3C3DE3
compress_test.compress('DDAEE') #DDAEE
compress_test.compress('DDAEEEE') #DDAEEEE
