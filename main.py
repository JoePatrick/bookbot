import sys
from stats import get_word_count, get_letter_count, get_sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    letter_sort = get_sorted_dict(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in letter_sort:
        if i["letter"].isalpha():
            print(f"{i["letter"]}: {i["count"]}")

    

main()

