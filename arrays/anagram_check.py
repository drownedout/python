"""
===============
Anagram check
===============

Given two strings, check to see if they're anagrams of each other.

"""

# Not optimal in interview
def anagram_check_one(string_one, string_two):
    string_one = string_one.replace(' ', '').lower()
    string_two = string_two.replace(' ', '').lower()

    # Edge case check
    if len(string_one) != len(string_two):
        return False

    return sorted(string_one) == sorted(string_two)


print(anagram_check_one('goooogd', 'dogg'))


# More manual solution
def anagram_check_two(string_one, string_two):
    string_one = string_one.replace(' ', '').lower()
    string_two = string_two.replace(' ', '').lower()

    # Edge case check
    if len(string_one) != len(string_two):
        return False

    count = {}

    # Adding string one letter counts to dictionary of count
    for letter in string_one:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in string_two:
        if letter in count:
            count[letter] -= 1
        else:
            return False  # If letter exists outside of string_one, it's false

    for k in count:
        if count[k] > 0:
            return False

    return True


print(anagram_check_two('goooogd', 'dogg'))
print(anagram_check_two('dog', 'dog'))
print(anagram_check_two('ball', 'la lb'))
