import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = count_words(text)
    counts = count_characters(text)
    sorted = sort_characters(counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for s in sorted:
        if s["char"].isalpha():
            print(f"{s["char"]}: {s["num"]}")
    print("============= END ===============")

main()