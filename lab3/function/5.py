#Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations
# 1
def all_permutations(n):
    #m = sorted(n)
    return list(permutations(n))

n = input()
print(all_permutations(n))
# 2
def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    perms = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i] + nums[i+1:]
        for p in permutations(remaining):
            perms.append([current] + p)
    return perms

nums = [1, 2, 3]
print(permutations(nums))