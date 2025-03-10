def get_book_text(filepath):
    with open(filepath) as f: #open file in variable f
        return f.read() #returns file as string

def count_words(string):
    words = string.split()
    return len(words)

def main():
    book = get_book_text("books/frankenstein.txt")
    count = count_words(book)
    print(f"{count} words found in the document")

main()