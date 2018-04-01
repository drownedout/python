"""
===============
Array Reversal
===============

Reverse an array - remove leading or ending whitespace.
"""

# Valid solutions but kinda cheating
def reversal(string):
    return " ".join(reversed(string.split()))


def reversal2(string):
    return " ".join(string.split()[::-1])


# Long form
def reversal3(string):
    words = []  # Empty list
    length = len(string)  # Length of string
    space = [' ']

    i = 0

    # While we haven't gone through string
    while i < length:
        if string[i] not in space:

            word_start = i

            # Keep going until we hit a space
            while i < length and string[i] not in space:
                i += 1

            # Append any part of the string between word start and i
            words.append(string[word_start:i])

        i += 1

    # Join the words together in reverse with spaces inbetween
    return " ".join(reversed(words))


print(reversal("this is great"))
print(reversal2("this is great   "))
print(reversal3("   this is great   "))
