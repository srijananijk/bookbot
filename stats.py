# Counts the number of words in a text
def count_words(text):
    words = text.split()
    return len(words)

# Counts the occurrences of each character in a text
def char_count(text):
    input_text = text.lower()
    letter_count = {}
    for letter in input_text:
        if letter in letter_count:
            continue
        else:
            count_val = input_text.count(letter)
            letter_count[letter] = count_val
    return letter_count

# Sorts a dictionary of character counts into a list of dictionaries sorted by count in descending order
def sort_dict(unsorted_dict):
    final_list =[]
    for key in unsorted_dict:
        if key.isalpha() is False:
            continue
        item_dict = {"char": key, "num": unsorted_dict[key]}
        final_list.append(item_dict)
    final_list.sort(key=lambda x: x["num"], reverse=True)
    return final_list