"""
String compression

Given a string in the form 'AAAABBBBCCCDDEE' compresses it into
become 'A4B4C3D2E2'

The function is case sensative so 'aaaAA' would return 'a3A2'

"""

# My original solution


def compress(string):
    last_letter = string[0]
    count = 0
    new_string = ''
    for i in string:
        if i == last_letter:
            count += 1
        else:
            new_string += last_letter
            new_string += str(count)
            last_letter = i
            count = 1
    new_string += last_letter
    new_string += str(count)

    print(new_string)


compress('AAAABBBBCCCDDEEEEE')

# Alternative solution - run length compression algorithm
# Very similar to original solutions
def compress_two(string):
    run = ""
    length = len(string)

    if length == 0:
        return ""
    if length == 1:
        return string + "1"

    last = string[0]
    count = 1
    index = 1

    while index < length:
        if string[index] == string[index - 1]:
            count += 1
        else:
            run = run + string[index - 1] + str(count)
            count = 1
        index += 1

    run = run + string[index - 1] + str(count)
    print(run)


compress_two('AAAABBBBCCCDDEEEEE')
