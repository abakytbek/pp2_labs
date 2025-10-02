# Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
def histogram(nums):
    for i in nums:
        print("*" * i)
            

nums = []
n = int(input("How many nums: "))
for i in range(n):
    temp = int(input())
    nums.append(temp)
histogram(nums)