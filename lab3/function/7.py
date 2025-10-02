# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] == 3:
            return True
    return False

nums = []
n = int(input("How many nums: "))
for i in range(n):
    temp = int(input())
    nums.append(temp)
if has_33(nums):
    print("True")
else:
    print("False")