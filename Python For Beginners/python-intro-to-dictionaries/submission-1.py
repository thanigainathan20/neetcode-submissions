from typing import List, Dict


def create_dict(name: str, age: int) -> Dict[str, int]:
    my_dict = {}
    my_dict[name] = age
    return my_dict


def new_dictionary(name: str, book_name: int) -> Dict[str, int]:
    new_dict = {}
    new_dict[name] = book_name
    return new_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    my_dict = {}
    for i in range(len(words)):
        my_dict[words[i]] = i
    return my_dict


# don't modify code below this line
print(new_dictionary("Alice", 25))
print(new_dictionary("Jane", 35))
print(new_dictionary("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))