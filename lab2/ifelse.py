# If ... Else
# Python supports the usual logical conditions from mathematics:
# Equals:                       a == b
# Not Equals:                   a != b
# Less than:                    a < b
# Less than or equal to:        a <= b
# Greater than:                 a > b
# Greater than or equal to:     a >= b

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
# And
if a > b and c > a:
  print("Both conditions are True")
# Or
if a > b or a > c:
  print("At least one of the conditions is True")
# Not
if not a > b:
  print("a is NOT greater than b")