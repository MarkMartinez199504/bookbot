import sys
from stats import count_words
from stats import count_chars
from stats import sort_dic


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(sys.argv[1]))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_count = count_chars(get_book_text(sys.argv[1]))

    sorted_chars = sort_dic(char_count)


main()


