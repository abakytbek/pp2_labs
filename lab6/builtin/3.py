text = input("enter a string: ")

cleaned = text.replace(" ", "").lower()

if cleaned == ''.join(reversed(cleaned)):
    print("palindrome")
else:
    print("not palindrome.")
