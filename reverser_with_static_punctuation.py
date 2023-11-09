def reverser(s):
    first_index = 0
    second_index = len(s) - 1
    print(second_index - first_index)
    while not (second_index - first_index) <= 1:
        if is_punctuation(s, first_index):
            first_index += 1

        if is_punctuation(s, second_index):
            second_index -= 1

        s = swap(s, first_index, second_index)

        first_index += 1
        second_index -= 1

    return s


def swap(s, first, second):
    s = s[:first] + s[second: second + 1] + s[first:]
    s = s[second:] + s[:second]
    return s[:second] + s[first: first + 1] + s[:second]


def is_punctuation(s, index):
    char = s[index]
    ascii_val = ord(char)
    if (64 < ascii_val < 91) | (96 < ascii_val < 123):
        return False
    else:
        return True


print(reverser("hello, this is ben."))
