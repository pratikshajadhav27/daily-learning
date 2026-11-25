def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest