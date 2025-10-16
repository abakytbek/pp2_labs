import re

text = "life_is_better_with_music"
pattern = r"_([a-z])"

def repl(match):
    return match.group(1).upper()

result = re.sub(pattern, repl, text)
print(result)
