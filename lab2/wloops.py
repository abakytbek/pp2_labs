# While Loops
# Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1

# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break                   # With the break statement we can stop the loop even if the while condition is true
  i += 1

# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue                # With the continue statement we can stop the current iteration, and continue with the next:
  print(i)

# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:                       # With the else statement we can run a block of code once when the condition no longer is true:
  print("i is no longer less than 6")