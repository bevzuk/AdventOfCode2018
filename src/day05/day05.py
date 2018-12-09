import re
from string import ascii_lowercase


def reduce(s):
    r = ""
    for char in ascii_lowercase:
        r += "(" + char + char.upper() + ")|"
    for char in ascii_lowercase:
        r += "(" + char.upper() + char + ")|"
    r = r[:-1]

    match = re.search(r, s)
    while match is not None:
        s = re.sub(r, "", s)
        match = re.search(r, s)

    return s


file = open("day05.input.txt", "r")
polymer = file.read()
file.close()

reduced = reduce(polymer)
print(reduced)
print("task 1: ", len(reduced))

min_len = len(polymer)
print(min_len)
for char in ascii_lowercase:
    polymer_with_removed_char = polymer.replace(char, "").replace(char.upper(), "")
    reduced = reduce(polymer_with_removed_char)
    print(char, len(reduced))
    if len(reduced) < min_len:
        min_len = len(reduced)
print("task 2: ", min_len)
