"""
===============
Missing Element
===============

Find the missing element in array
"""

import collections

# First solution
def missing(array1, array2):
    for i in array1:
        if i not in array2:
            print(i)


missing([1, 2, 3, 4, 5, 6, 7, 8], [3, 7, 2, 1, 4, 6])


# Second solution O(nlogn)
def missing_two(array1, array2):
    array1.sort()
    array2.sort()

    # Zip matches elements in two arrays and zips them into tuples
    # Example: zip([1,2,3],[4,5,6]) -> [(1,4),(2,5),(3,6)]
    for num1, num2 in zip(array1, array2):
        if num1 != num2:
            return num1

    # Returns last element since all previous elements matched
    return array1[-1]


# Linear time solution, needs the 'collections' module
def missing_three(array1, array2):
    d = collections.defaultdict(int)  # Prevents key error if key doesn't exist

    for number in array2:
        d[number] += 1  # Adds a count for every instance of a number

    for number in array1:
        if d[number] == 0:  # Number doesn't exist in array2, return missing number
            return number
        else:
            d[number] -= 1  # Decreases count for every intance of a number


# You could also count the sums of each array and subtract their values against each
# other, the difference would be the missing number. However, this
# might be problematic with large sets or with floats.
def missing_four(array1, array2):
    result = 0

    # Peform an XOR between the numbers in the arrays
    for number in array1 + array2:  # for i in concat array
        result ^= number  # XOR with number
        print(result)

    return result
