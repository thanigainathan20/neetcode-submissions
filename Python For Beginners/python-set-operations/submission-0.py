from typing import List

def count_unique_words(words: List[str]) -> int:
    set_word = set()  # Use set() instead of {}
    for word in words:  # Iterate directly over words instead of indices
        set_word.add(word)
    return len(set_word)  # Return the count, not the set itself

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))