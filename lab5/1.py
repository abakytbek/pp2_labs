import re

def match_string(s):
    pattern = r"ab*"

    if re.fullmatch(pattern, s):
        return True
    else:
        return False

test_strings = ["a", "abb", "abbbbb", "aa", "bba", "abx", ""]

for i in test_strings:
    print(f"'{i}': {match_string(i)}")
