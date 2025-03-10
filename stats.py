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

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list