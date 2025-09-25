import sys 
from stats import count_words, char_count, sort_dict 

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
def main():
    if(len(sys.argv) != 2): # Getting input from CLI
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    
    # Word count
    num_words = count_words(book_text)

    # Character count
    char_counts = char_count(book_text)
    # Sorted character count
    final_lst = sort_dict(char_counts)

    #Final output
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count ----------")
    for item in final_lst:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()