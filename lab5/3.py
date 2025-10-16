import re

def check(s):
    pattern = r"[a-z]+_[a-z]+"
    if re.search(pattern, s):
        return True
    else:
        return False

test_strings = [
    "hello_world",
    "python_learn",
    "snake_snake",
    "data_123",
    "week_midterm",
    "user_user",
    "_hidden_name"
]

for s in test_strings:
    print(f"'{s}': {check(s)}")
