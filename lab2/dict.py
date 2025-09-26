# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)                     # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)                     # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print(len(thisdict))                # 3
print(type(thisdict))               # <class 'dict'>

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)                     # {'name': 'John', 'age': 36, 'country': 'Norway'}


#           Access Dictionary Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])            # Ford
x = thisdict.get("model")
print(x)                            # Mustang
x = thisdict.keys()
print(x)                            # dict_keys(['brand', 'model', 'year'])
x = thisdict.values()
print(x)                            # dict_values(['Ford', 'Mustang', 1964])
x = thisdict.items()
print(x)                            # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


#           Change
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car) #before the change       # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car["year"] = 2020
print(car) #after the change        # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)                     # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


#           Add
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car) #before the change       # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car["color"] = "red"
print(car) #after the change        # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)                     # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


#           Remove
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")               # pop() method removes the item with the specified key name
print(thisdict)                     # {'brand': 'Ford', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()                  # popitem() method removes the last inserted item
print(thisdict)                     # {'brand': 'Ford', 'model': 'Mustang'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]               # del keyword removes the item with the specified key name
print(thisdict)                     # {'brand': 'Ford', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()                    # clear() method empties the dictionary
print(thisdict)                     # {}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes")                      # Yes


#           Loop
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}                                   # brand
for x in thisdict:                  # model
  print(x)                          # year

                                    # Ford
for x in thisdict:                  # Mustang
  print(thisdict[x])                # 1964

# values() method to return values of a dictionary
                                    # Ford
for x in thisdict.values():         # Mustang
  print(x)                          # 1964

# keys() method to return the keys of a dictionary
                                    # brand
for x in thisdict.keys():           # model
  print(x)                          # year

                                    # brand Ford
for x, y in thisdict.items():       # model Mustang
  print(x, y)                       # year 1964


#           Copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
new1 = thisdict.copy()
print(new1)                         # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
new2 = dict(thisdict)
print(new2)                         # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


#           Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)                     # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)                     # {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
print(myfamily["child2"]["name"])   # Tobias

for x, obj in myfamily.items():     # child1
    print(x)                        # name: Emil
    for y in obj:                   # year: 2004
        print(y + ':', obj[y])      # child2
                                    # name: Tobias
                                    # year: 2007
                                    # child3
                                    # name: Linus
                                    # year: 2011


#           Dictionary Methods
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()	        Removes the last inserted key-value pair
# setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary