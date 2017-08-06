# Fizz Buzz takes in an integer and creates a string represenation from 1 to n
# Multiples of 3 == 'Fizz'
# Multiples of 5 == 'Buzz'
# Multiples of 3 and 5 == 'FizzBuzz'

# Assumptions
	# Can't assume inputs are valid

class Fizz(object):

	def fizz_buzz(self, number):
		# Does not assume inputs are valid
		if type(number) is str:
			raise TypeError('Number cannot be a string')
		if number is None:
			raise TypeError('Number cannot be none')
		if number < 1:
			raise ValueError('Number must be greater than zero')

		results = []

		for i in range(number + 1):
			# Checks to see if i is divisible by 5 and 3.
			# You could also use i % 15 == 0
			# You must set this as the first case or else the function
			# won't return the proper value
			if i % 5 and i % 3 == 0:
				results.append("FizzBuzz")
			elif i % 5 == 0:
				results.append("Buzz")
			elif i % 3 == 0:
				results.append("Fizz")
			else:
				results.append(str(i)) # Coercing i into a string

		# Returns list with values
		return results

fizz_test = Fizz()

fizz_test.fizz_buzz(22) #['Buzz', '1', '2', 'FizzBuzz', '4', 'Buzz', 'FizzBuzz', 
# '7', '8', 'FizzBuzz', 'Buzz', '11', 'FizzBuzz', '13', '14', 'Buzz', '16', '17', 
# 'FizzBuzz', '19', 'Buzz', 'FizzBuzz', '22']

fizz_test.fizz_buzz('string') # Throws TypeError
fizz_test.fizz_buzz(None) # Throws TypeError
fizz_test.fizz_buzz(0) # Throws ValueError