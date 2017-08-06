# Recursion of aggregating integers (ex: 4 + 3 + 2 + 1 + 0 = 0)

def rec_sum(n):
	# base case
    if n == 0:
        return 0
    # recursive call
    else:
    	# if n has not reached zero, the current value will return
    	# n + rec_sum(n-1)
        return n + rec_sum(n-1)


"""

Example:

rec_sum(4)

We end the recursive calls with the value of 0 once n has reached 0.
Below is the returned value against the value of rec_sum(n) in reverse.

n = 0, value = 0
n = 1, value = 0 + 1 (1)
n = 2, value = 0 + 1 + 2 (3)
n = 3, value = 0 + 1 + 2 + 3 (6)
n = 4, value = 0 + 1 + 2 + 3 + 4 (10)

"""