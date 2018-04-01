"""
Determine if a string is made up of all unique characters.
"""

# My original solution
def unique(string):
    temp = ""
    for i in string:
        if i in temp:
            print('Not unique')
            return False
        temp += i
    print('Unique')
    return True


# Alternative using sets
# Documentation on sets in Python
# https://docs.python.org/2/library/sets.html
def unique_two(string):
    return len(set(string)) == len(string)


# Another alternative solution
def unique_three(string):
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            char.add(letter)
    return True


unique('it works')  # True
unique('this is not unique')  # False
unique('catdog')  # True
