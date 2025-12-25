def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}
    for c in text:
        char = c.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_num_key(dict):
    return dict["num"]

def sort_characters(char_counts):
    unsorted = []
    for char in char_counts:
        unsorted.append({"char": char, "num": char_counts[char]})
    unsorted.sort(reverse=True, key=get_num_key)
    return unsorted