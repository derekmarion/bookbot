def main():
    book_path = "books/frankenstein.txt"
    text = read_file(book_path)
    quantity_words = count_words(text)
    quantity_letters = count_characters(text)
    generate_report(book_path, quantity_words, quantity_letters)


def count_words(text):
    """counts number of words in input string"""
    words = text.split()
    return len(words)


def read_file(path):
    """reads file from stdin to string"""
    with open(path) as f:
        return f.read()


def count_characters(text):
    """counts characters in text and returns sorted dictionary of values"""
    output = {}
    for char in text:
        if char.lower() not in output and char.lower().isalpha():
            output[char.lower()] = 1
        elif char.lower().isalpha():
            output[char.lower()] += 1
    output = aggregate_character_counts(output)
    output.sort(reverse=True, key=sort_on)
    return output


def aggregate_character_counts(dict):
    """turns dictionary counts of characters into a list of dictionaries for sorting"""
    list_of_dicts = []
    for k, v in dict.items():
        character_count = {}
        character_count["character"] = k
        character_count["quantity"] = v
        list_of_dicts.append(character_count)
    return list_of_dicts


def sort_on(dict):
    """returns key for sort method of dictionary of character counts"""
    return dict["quantity"]


def generate_report(book, words, chars):
    """Generates a text report of character and words count"""
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    for char in chars:
        print(
            f"'{char['character']}' was found in the document {char['quantity']} times"
        )
    print("--- End report ---")


main()
