# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    temp = [0, 0, 7]
    for i in range(len(nums)):
        if nums[i] == temp[0]:
            temp.pop(0)
    if not temp:
        return True
    return False

nums = []
n = int(input("How many nums: "))
for i in range(n):
    temp = int(input())
    nums.append(temp)
if spy_game(nums):
    print("True")
else:
    print("False")