thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry', 'apple', 'cherry']

#List lenth
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#['apple', 'banana', 'cherry']
#[1, 5, 7, 9, 3]
#[True, False, False]

list1 = ["abc", 34, True, 40, "male"] #['abc', 34, True, 40, 'male']

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'>

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#['apple', 'banana', 'cherry']

