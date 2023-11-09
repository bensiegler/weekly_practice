def reverser(s):
    first_word_start = 0
    second_word_start = s.rfind(" ")
    first_word_end = first_word_start
    second_word_end = second_word_start + 1

    while True:
        while not s[first_word_start].isalpha():
            first_word_start += 1
        first_word_end = first_word_start

        while not s[second_word_start].isalpha():
            second_word_start += 1
        second_word_end = second_word_start

        while s[first_word_end].isalpha():
            first_word_end += 1

        while s[second_word_end].isalpha():
            second_word_end += 1

        if (second_word_start - first_word_end) <= 1:
            break

        first_word = s[first_word_start:first_word_end]
        second_word = s[second_word_start:second_word_end]
        index_adjustment = len(first_word) - len(second_word)
        s = s[:second_word_start] + first_word + s[second_word_end:]
        s = s[:first_word_start] + second_word + s[first_word_end:]

        first_word_start = first_word_end - index_adjustment
        prev_second_word_start = second_word_start - index_adjustment
        while second_word_start >= prev_second_word_start:
            second_word_start = s.rfind(" ", None, second_word_start - 1) + 1

    return s


# print(reverser("hello, this is ben."))
print(reverser("hi I am tired"))
