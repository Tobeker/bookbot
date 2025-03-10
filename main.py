from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f: #open file in variable f
        return f.read() #returns file as string

def main():
    book = get_book_text("books/frankenstein.txt")
    count_w = count_words(book)
    count_c = count_characters(book)
    print(f"{count_w} words found in the document")
    print(count_c)

main()