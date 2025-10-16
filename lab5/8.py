import re

text = "StayWithMeForever"
result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)