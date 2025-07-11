def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    # Count the number of characters in the file contents, including whitespace and symbols.
    c_dict = {}
    lowercase_contents = file_contents.lower()
    for char in lowercase_contents:
        char.lower()
        if char in c_dict:
            c_dict[char] += 1
        else:
            c_dict[char] = 1
    return c_dict

def sort_on(dict):
    # Sort the dictionary by character frequency in descending order.
    return dict["num"]