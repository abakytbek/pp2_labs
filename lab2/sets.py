thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'banana', 'cherry', 'apple'}

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#{'banana', 'cherry', 'apple'}

#True/False and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#{True, 2, 'banana', 'cherry', 'apple'}

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #3

#Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}
#{True, 34, 40, 'male', 'abc'}

myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) #{'apple', 'banana', 'cherry'}

#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) #cherry apple banana

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) #False

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#{'cherry', 'banana', 'apple', 'orange'}

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

#Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#{'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#banana
#{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists


