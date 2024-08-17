from collections import Counter

def get_book_test(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(book_text):
    words = book_text.split()
    return len(words) 

# def count_characters(book_text):
    # all_lower = book_text.lower()
    # counted = Counter(all_lower)
    # return counted
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_test(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_number_of_words(text)} words found in the document")
    characters = get_chars_dict(text)
    tuples = list(characters.items())
    for tuple in tuples:
        if tuple[0].isalpha():
            print(f"The '{tuple[0]}' character was found {tuple[1]} times")
        
        

main()