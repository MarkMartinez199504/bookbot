def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    
    return contents

def count_words(text):
    words = text.split()
    return len(words)


def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    print(f"Found {word_count} total words")



main()


