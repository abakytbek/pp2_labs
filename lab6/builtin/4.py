import time, math

n = int(input())
t = int(input())

time.sleep(t / 1000)
print(f"square root of {n} after {t} miliseconds is {math.sqrt(n)}")
