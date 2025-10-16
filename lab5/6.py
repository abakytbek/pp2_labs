import re

text_to_match = "When you try your best but you don't succeed, when you get what you want but not what you need."

pattern = r"[ ,.?]"
result = re.sub(pattern, ":", text_to_match)
print(result)
