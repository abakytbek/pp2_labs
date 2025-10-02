#You are given list of numbers separated by spaces. Write a function filter_prime
# which will take list of numbers as an agrument and returns only prime numbers from the list.

def which_prime(num):
    cnt = 0
    for i in range(1 ,num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return True

n = int(input("How many numbers: "))
nums = []
for i in range(n):
    temp = int(input())
    nums.append(temp)
for i in nums:
    if which_prime(i):
        print(i)
# №2
def which_prime2(nums, n):
    for i in range(n):
        cnt = 0
        for j in range(1, nums[i] + 1):
            if nums[i] % j == 0:
                cnt += 1
        if cnt == 2:
            print(nums[i])

n = int(input("How many numbers: "))
nums = []
for i in range(n):
    temp = int(input())
    nums.append(temp)
which_prime2(nums, n)