import re

letters = "cwd"
guess = "crossword"


def get_regex(word):
    pattern = ""
    letter_list = list(word)
    print("letter list is :", letter_list)
    for i in letter_list:
        pattern = pattern + ".*" + i
    pattern = pattern + ".*"
    print("pattern returned is: ", pattern)
    return pattern


res = re.search(get_regex(letters), guess)
if res:
    print("yes")
else:
    print("no")
