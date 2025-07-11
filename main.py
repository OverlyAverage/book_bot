import sys
from stats import word_count, char_count, sort_on

def get_book_text(file_path):
   #Read the contents of a book file and return it as a string.

    with open(file_path) as file:
        file_contents = file.read()

        return file_contents

def report(file_path, word_count, char_count):
    # Print a report of the word and character counts.
    conv_list = [{"char": key, "num": value} for key, value in char_count.items()]
    conv_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count -------")
    for item in conv_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def main():
   # print(f"{word_count(get_book_text("books/frankenstein.txt"))} words found in the document.")
   # print(char_count(get_book_text('books/frankenstein.txt')))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report(sys.argv[1], word_count(get_book_text(sys.argv[1])), char_count(get_book_text(sys.argv[1])))

main()
 