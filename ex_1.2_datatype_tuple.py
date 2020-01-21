'''
author: bhoj bahadur karki
date: 2020-jan-19th
purpose : about tuple in python

Tuple: A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The differences between tuples and lists are, the tuples 
cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

creation: using ()

Tuple defination by python.org:
Tuples

Tuples are immutable sequences, typically used to store collections of heterogeneous 
data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases 
where an immutable sequence of homogeneous data is needed (such as allowing storage in 
a set or dict instance).

class tuple([iterable])

Tuples may be constructed in a number of ways:

    1. Using a pair of parentheses to denote the empty tuple: ()

    2. Using a trailing comma for a singleton tuple: a, or (a,)

    3. Separating items with commas: a, b, c or (a, b, c)

    4. Using the tuple() built-in: tuple() or tuple(iterable)

'''
# Tuple creation various ways
t1 = () # tuple
t2 = "a", # also tuple
t3 = ("a","b","c") #tuple
t4= "a","b","c"  # tuple
t5 = tuple([2,3,4])  

print("t1=",type(t1),t1)
print("t2=",type(t2),t2)
print("t3=",type(t3),t3)
print("t4=",type(t4),t4)
print("t5=",type(t5),t5)


a,b = 200,300  # Note tuple but multiple variable in single line
print(a,b)


#----------------- accessing elements of tuple----------------------
t = (2,3,4,"five",4.5,False); # note: semicolons are optional in python
print(t[0])

# ---------------Updating tuple----------------
# Not valid
# t[0]=100 # TypeError: 'tuple' object does not support item assignment

# ---------------Tuple slicing-----------------
print(t[1:4]) # prints 3, 4, 'five'

# ---------------------Changing tuple items(generally not changeable)---
'''
Changing a Tuple
Unlike lists, tuples are immutable(unchangable).

This means that elements of a tuple cannot be changed once it has been assigned. 
But, if the element is itself a mutable datatype like list, 
its nested items can be changed.

We can also assign a tuple to different values (reassignment).

'''
ta = "a","b",[2,3,4]
print(ta)
# Not valie
# ta[0]=4

# Valid
ta[2][0]= 77
print("changed=",ta)

# ------------Deleting a tuple---------------
# we use del operator to delete a tuple

# del ta[0] #TypeError: 'tuple' object doesn't support item deletion
# print(ta)

del ta
# print(ta) # NameError: name 'ta' is not defined


# ---------------Adding two tuple-------
# we can use + operator to combine a tuple i.e. concatination
result = (2,3,4)+(33,44,55)
print("result = ",result)

'''
Advantages of Tuple over List
Since tuples are quite similar to lists, both of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. Below listed are 
some of the main advantages:

1. We generally use tuple for heterogeneous (different) datatypes and 
list for homogeneous (similar) datatypes.

2. Since tuples are immutable, iterating through tuple is faster than with list. 
So there is a slight performance boost.

3. Tuples that contain immutable elements can be used as a key for a dictionary. 
With lists, this is not possible.

4. If you have data that doesn't change, implementing it as tuple will guarantee 
that it remains write-protected.
'''

# various operation
# ---------Membership test (test if an element is in tuple)-----------
x = (2,3,4)
print("is 2 present in x=",2 in x)
print("is 55 present in x=",55 in x)


'''
Python Expression	           Results	                        Description

len((1, 2, 3))	               3	                            Length
(1, 2, 3) + (4, 5, 6)	       (1, 2, 3, 4, 5, 6)	            Concatenation
('Hi!',) * 4	               ('Hi!', 'Hi!', 'Hi!', 'Hi!')	    Repetition
3 in (1, 2, 3)	                True	                        Membership
for x in (1, 2, 3): print x,	1 2 3	                        Iteration
'''

print(len((1, 2, 3)))
print((1, 2, 3) + (4, 5, 6))
print(('Hi!',) * 4)
print(3 in (1, 2, 3))
for x in (1, 2, 3): print(x); # semi colon is optional