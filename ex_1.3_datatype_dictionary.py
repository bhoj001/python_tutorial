'''
author: bhoj bahadur karki
date: 2020-jan-19th
purpose : about dictionary in python

Dictionary: Python dictionary is an unordered collection of items. 
While other compound data types have only value as an element, a dictionary has a key: value pair.

Dictionaries are optimized to retrieve values when the key is known.

PythonOrg def:
Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. 
Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, 
which can be any immutable type; strings and numbers can always be keys. Tuples can be 
used as keys if they contain only strings, numbers, or tuples; if a tuple contains any 
mutable object either directly or indirectly, it cannot be used as a key. You can’t use 
lists as keys, since lists can be 
modified in place using index assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement 
that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. 
Placing a comma-separated list of key:value pairs within the braces adds 
initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting 
the value given the key. It is also possible to delete a key:value pair with del. 
If you store using a key that is already in use, the old value associated with that key is forgotten. 
It is an error to extract a value using a non-existent key.

Note: dictionary has key,value
key can be integer, string, float but it has to be unique
>>> x = {2:30,3:2,2:40}  # if we repeat a key, one item(here 2:30) is ignored
>>> x 
{2: 40, 3: 2}
'''

# -------Creating dictionary------------
# using {}
tel = {'jack': 4098, 'sape': 4139}
tel['mike'] = 4127 # adding to dictionary
print("tel=",tel)

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print("my_dict=",my_dict)
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print("my_dict=",my_dict)

# using dict() keyword
x= dict([('juli', 4139), ('max', 4127), ('jack', 4098)])
print("x=",x)

a = {x: x**2 for x in (2, 4, 6)}
print("a=",a)

# --------Accessing element in dictionary-------
# we use key to access element in dictionary e.g. dic[key]
print("juli  =",x['juli'])

# ---------Changing element in dictionary-----
# we use equal sign with syntax: dict[key]=value
x['juli'] = 3
print("new x = ",x)

# -------deleting item in dictionary----------
# using  dict.pop(key)
x.pop('juli') # this will remove key-value pair of juli(juli:3)
print("after pop x = ",x)

# using del dict[key]
del x['max']
print("after del x = ",x)

# using .clear() to clear all items
x.clear() # this will empty the dictionary 
print("after clear x=",x)
# ----------Looping technique in dictionary---------
knights = {'ram': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# ------for  sequence datatype like list, tuple, range-------

#------getting index value from sequence datatype like list, tuple, range-------
# use enumerate() function
# When looping through a sequence, the position index and corresponding value can 
# be retrieved at the same time using the enumerate() function.

# i =index, v= value, in short form
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# -------combine two list and loop------------
# To loop over two or more sequences at the same time, the entries can be paired with 
# the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['Bhoj', 'to teach programming', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#-------- reversing a sequence datatype # range syntax: range(start:int, end:int, step:int)
for item in reversed(range(2,10,2)):
    print(item)

# ---------Loop via sorting an item------------
# To loop over a sequence in sorted order, use the sorted() function 
# which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# here set() function removes the duplicate items
for f in sorted(set(basket)):
    print(f)


'''
Method	            Description

clear()	        Remove all items form the dictionary.
copy()	        Return a shallow copy of the dictionary.
fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
items()	        Return a new view of the dictionary's items (key, value).
keys()	        Return a new view of the dictionary's keys.
pop(key[,d])	Remove the item with key and return its value or d if key is not found. 
                If d is not provided and key is not found, raises KeyError.
popitem()	    Remove and return an arbitary item (key, value). Raises KeyError if the dictionary 
                is empty.
setdefault(key[,d])	If key is in the dictionary, return its value. If not, 
                    insert key with a value of d and return d (defaults to None).
update([other])	Update the dictionary with the key/value pairs from other, 
                overwriting existing keys.
values()	    Return a new view of the dictionary's values
'''