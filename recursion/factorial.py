def factorial(n):
    # Base case
    if n == 0:
        return 1;
    # Recursive call
    else:
    	# Calls itself again multiplying n's current value
    	# against the value of factorial of (n-1)
        return n * factorial(n-1)	

"""

Example:

factorial(4)

We end the recursive calls with the value of 1 once n has reached 0.
Below is the returned value against the value of factorial(n) in reverse.

n = 0, value = 1
n = 1, value = 1 * 1 (1)
n = 2, value = 1 * 1 * 2 (2)
n = 3, value = 1 * 1 * 2 * 3 (6)
n = 4, value = 1 * 1 * 2 * 3 * 4 (24)


"""