from stats import count_words
from stats import count_chars

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {word_count} total words")

    char_count = count_chars(get_book_text("books/frankenstein.txt"))
    print(char_count)


main()


