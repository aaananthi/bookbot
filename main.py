import sys

from stats import get_num_words, get_character_count

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    with open(sys.argv[1]) as f:
        file_contents = f.read()
        get_num_words(file_contents)
        get_character_count(file_contents)

get_book_text()