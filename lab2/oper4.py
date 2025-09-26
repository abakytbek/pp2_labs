#Python Identity Operators
#is - Returns True if both variables are the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#is not	- Returns True if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) # returns False because z is the same object as x

print(x is not y) # returns True because x is not the same object as y, even if they have the same content

print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y



#Python Membership Operators
#in - Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
print("banana" in x) # returns True because a sequence with the value "banana" is in the list

#not in	- Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list


#Python Bitwise Operators
#& 	AND	Sets each bit to 1 if both bits are 1
print(6 & 3) #2

#|	OR	Sets each bit to 1 if one of two bits is 1
print(6 | 3) #7

#^	XOR	Sets each bit to 1 if only one of two bits is 1
print(6 ^ 3) #5

#~	NOT	Inverts all the bits
print(~3) #-4

#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3 << 2) #12

#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(8 >> 2) #2

#Operator Precedence
print((6 + 3) - (6 + 3)) #0
print(100 + 5 * 3) #115

#()	Parentheses

#**	Exponentiation
print(100 - 3 ** 3) #73

#+x  -x  ~x	Unary plus, unary minus, and bitwise NOT
print(100 + ~3) #96

#*  /  //  %	Multiplication, division, floor division, and modulus
print(100 + 5 * 3) #115

#+  -	Addition and subtraction
print(100 - 5 * 3) #85

#<<  >>	Bitwise left and right shifts
print(8 >> 4 - 2) #2

#&	Bitwise AND
print(6 & 2 + 1) #2

#^	Bitwise XOR
print(6 ^ 2 + 1) #5

#|	Bitwise OR
print(6 | 2 + 1) #7

#==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators
print(5 == 4 + 1) #True

#not	Logical NOT
print(not 5 == 5) #False

#and	AND
print(1 or 2 and 3) #1

#or	OR
print(4 or 5 + 10 or 8) #4
