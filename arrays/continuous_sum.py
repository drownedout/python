"""
Given an array of integers, find the largest continous sum
"""

# First solution
def cont_sum(array):
	result1 = 0
	result2 = 0

	for i in array:
		result1 += i
		if result1 >= result2:
			result2 = result1
			print(result2)

	print(result2)

cont_sum([1,2,-1,3,4,10,10,-10, 10, 12, 1])


# Second solution

def cont_sum2(array):
	if len(array) == 0:
		return 0

	# Set both max and current to first element
	max_sum = current_sum = array[0]

	# Start from the second elem
	for num in array[1:]:
		current_sum = max(current_sum + num, num) # sets current equal to whichever is higher, this is for cases if the current is negative
		max_sum = max(current_sum, max_sum) # sets max to whichever is higher

	return max_sum

print(cont_sum2([1,2,-1,3,4,10,10,-10, 10, 12, 1]))