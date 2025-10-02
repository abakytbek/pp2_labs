# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Note: don't use collection set.
def Unique(nums):
    new1 = []
    new2 = nums
    new2.sort()
    if len(new2) > 0:  
        new1.append(new2[0])
    for i in range(1, len(nums)):
        if new2[i - 1] != new2[i]:
            new1.append(nums[i])
    return new1

nums = []
n = int(input("How many nums: "))
for i in range(n):
    temp = int(input())
    nums.append(temp)
print(Unique(nums))