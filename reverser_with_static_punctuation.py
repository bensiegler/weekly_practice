def reverser(s):
    first_word_start = 0
    second_word_start = s.rfind(" ")
    first_word_end = first_word_start
    second_word_end = second_word_start + 1

    while not (second_word_start - first_word_start) <= 1:

        while s[first_word_end].isalpha():
            first_word_end += 1

        while s[second_word_end].isalpha():
            second_word_end += 1

        first_word = s[first_word_start:first_word_end]
        second_word = s[second_word_start:second_word_end]
        index_adjustment = len(first_word) - len(second_word)
        s = s[:first_word_start] + second_word + s[first_word_end:]
        s = s[:second_word_start] + first_word + s[second_word_end - index_adjustment:]

        first_word_start = first_word_end
        while not s[first_word_start].isalpha():
            first_word_start += 1

        second_word_start = s.rfind(" ", None, second_word_start)
        second_word_end = second_word_start
    return s


print(reverser("hello, this is ben."))
