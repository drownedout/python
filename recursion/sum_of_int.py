# Create a function which returns the sum of all individual digits in that integer.
# For example, 4321 would return 4+3+2+1

def sum_func(n):

	# base case
    if n < 10:
        return n
    else:
    	# Returns the remainder of n/10 and adds it to the value
    	# of sum_func((n-(n%10))/10), or (n - (the remainder of n/10)) divided by 10
        return n % 10 + sum_func((n-(n%10))/10)

"""

Example:

sum_func(321)

We end the recursive calls with the value of n itself once n is less than 10.
Once n's value falls below 10, we aggregate each value that was returned before it.
Below is the how the function would look if n had a value of 321.

321 % 10 + sum_func(321-(321%10)/10) => 1 + sum_func(32), value = 1
32 % 10 + sum_func(32-(32%10)/10) => 2 + sum_func(3), value = 1 + 2
n < 10 => 3, value = 1 + 2 + 3

sum_func(321) == 6

"""