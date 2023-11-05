
def reverser(s):
    words = s.split(" ")
    swapped = ""

    for i in range(1, len(words) + 1):
        end = len(words) - i
        start = i
        first_word = words[start]
        last_word = words[end]


def punctuation_swapper(source_word, output_word):
    for j in range(len(source_word)):
        ascii_val = ord(source_word[j])
        if not ((ascii_val > 64 & ascii_val < 91) | (ascii_val > 96 & ascii_val < 123)):
            if j > len(source_word) / 2:
                output_word += chr(ascii_val)
            else:
                output_word = chr(ascii_val) + output_word
            source_word = source_word[:j] + source_word[j:]
    return source_word, output_word


print(reverser("hello, this is ben."))

