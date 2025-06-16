from stats import count_words, count_characters, sort_character_counts
import sys

def get_book_text(filepath):
    with open(filepath) as book_file:
        book_contents = book_file.read()
    return book_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    frankenstein = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count -----------")
    count_words(frankenstein)
    print("---------- Character Count ----------")
    characters_dict = count_characters(frankenstein)
    sort_character_counts(characters_dict)
    print("============= END ===============")



main()