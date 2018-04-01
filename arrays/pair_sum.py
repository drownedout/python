"""
===============
Pair Sum
===============

Given an integer array, output all of the unique pairs that sum up to a
specific k.

"""

# Original solution
def pair_sum_one(array, value):
    if len(array) < 2:
        return

    sets = set()

    for i in range(len(array)):
        for n in range(len(array) - 1):
            if i != n and array[i] + array[n] == value:
                sets.add((array[i], array[n]))
    print(sets)


def pair_sum_two(array, value):

    # Edge case
    if len(array) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    for number in array:
        target = value - number  # Looking for the number that adds up to value

        if target not in seen:
            seen.add(number)
        else:
            output.add(((min(number, target)), max(number, target)))

    print(output)


pair_sum_one([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 10)
pair_sum_two([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9], 10)
