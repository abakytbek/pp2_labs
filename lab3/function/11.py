# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def Is_It_Palindrom(n):
    m = ""
    for i in range(len(n) - 1, -1, -1):
        m += n[i]
    if n == m:
        print("Yes")
    else:
        print("No")

n = input()
Is_It_Palindrom(n)