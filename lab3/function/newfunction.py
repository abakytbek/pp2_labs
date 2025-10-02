def grams_to_ounces(grams):
    return grams / 28.3495231

def fahrenheit_to_centigrade(f):
    return (5/9) * (f - 32)

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]