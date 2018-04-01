"""
Implement a Fibonnaci Sequence in three different ways:

	 - Recursively
	 - Dynamically
	 - Iteratively


The function will accept a number 'n' and return the 'nth' number
of the Fibonnaci Sequence.

Example: 0,1,1,2,3,5,8,13,21 ...starts off with a base case checking
to see if n = 0 or 1, then it returns 1.

Else, it returns fib(n-1) + fib(n-2)

"""


# Recursive solution
# The recursive solution is exponential O(2^n), though very
# simple and is a basic implementation

def recursive_fib(num):

    # Base case
    if num == 0 or num == 1:
        return num
    # Recursive case
    else:
        return recursive_fib(num - 1) + recursive_fib(num - 2)


# Dynamic Solution
# Here we set the cache beforehand based on the desired 'n' number


# Instantiate cache information
number = 10
cache = [None] * (number + 1)


def dynamic_fib(num):

    # Base case
    if num == 0 or num == 1:
        return num

    # Check case
    if cache[num] is not None:
        return cache[num]

    # Keep setting cache
    cache[num] = dynamic_fib(num - 1) + dynamic_fib(num - 2)

    return cache[num]


# Iterative Solution
# A pythonic solution, takes advantage of tuple unpacking
def iterative_fib(num):

    # Set starting point
    a, b = 0, 1

    for i in range(num):
        # First loop: a = 1, b = 1
        # Second loop: a = 1, b = 2
        # Third loop: a = 2, b = 3
        # Four loop: a = 3, b = 5
        a, b = b, a + b  # Tuple unpacking

    return a


print(recursive_fib(10))  # 55
print(dynamic_fib(number))  # 55
print(iterative_fib(10))  # 55
