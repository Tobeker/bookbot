def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    text = string.lower()
    dict = {}
    for letter in text:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict