from stats import count_words
from stats import count_characters
from stats import sort_dict

import sys

def get_book_text(filepath):
    with open(filepath) as f: #open file in variable f
        return f.read() #returns file as string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book = get_book_text(path)
    count_w = count_words(book) #number of words in text
    count_c = count_characters(book) #number of each char
    list = sort_dict(count_c)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_w} total words")
    print("--------- Character Count -------")
    for char in list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()