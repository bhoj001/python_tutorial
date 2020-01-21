'''
author: bhoj bahadur karki
date: 2020-jan-17th
purpose : about list in python

List: stores data in dynamic list
creation: using [] or list()

usages: as stack, as queue

listb= lista #  {this is copy via reference}
# if you want a new fresh copy which is independent of lista in listb
# then do :
listb= lista.copy() # this copy methods copies all the element in new list
'''
# list creation
integer_list = [1,2,3,5,66,100]
# mixed types
first_list = ["one",1,2,3.4]
print(first_list[0])

# negative indexing
print("negaitve indexing=",first_list[-1])

l = list({2,3,4})
print(l)
print(type(l))

# ----------------------------------item addition in the list--------------------------
# list addition 
# 1. using .append() method
# syntax: list.append(obj)
first_list.append("33") # single item
first_list.append([44,55,66]) # adding using list multiple items
print("after addition=",first_list)

# 2. using .insert(index,obj) method
# syntax : list.insert(index, obj)
# Inserts object obj into list at offset index


# ------------------------Copying list to another list----------------------
second_list = first_list
print(second_list)
first_list[0]=55555
print("first list=",first_list)   
print("second list=",second_list) # second list will also have the same value as first list 
# This shows if one list if copied only the refrence is passed new value is not added

second_list[0]="Nepal"
print("first list=",first_list)
print("Second list=",second_list)

# --------------------Item extraction using slicing------------------------------

x = first_list[0:3]
print("sliced value=",x)
# elements from beginning to end:
y = first_list[:]
print("from begining to end: ",y)

# -------------------------------Deletion of members------------------------------
# using del keyword
list1 =  [2,3,4,5,6,7,8]
del list1[2];
print("list1=",list1)
lista = [2,3,4,5,6,7,9,8,19]
del lista[2:4]  # removes 4 and 5 from list
print("lista=",lista)

# using .remove() => using item , 
# .pop() => using item index
# ,.clear()
# syntax: remove(item_to_remove)
print("lista before .remove=",lista)
lista.remove(2)
print("lista after .remove=",lista)

# list.pop(obj=list[-1])
# Removes and returns last object or obj from list
# pass the index of which you want to pop
# syntax .pop(index_of_list)
print("lista before .pop=",lista)
lista.pop()
print("lista after .pop()=",lista)
lista.pop(0)
print("lista after .pop(0) i.e. remove of 0 index=",lista)

lista.clear()
print("lista after .clear=",lista)


# ---------------------useful function related with list----------------
# len(list)
# Gives the total length of the list.

# max(list)
# Returns item from the list with max value.

# min(list)
# Returns item from the list with min value.

# list(seq)
# Converts a tuple into list.

# list.reverse()
# Reverses objects of list in place

# list.sort([func])
# Sorts objects of list, use compare func if given

# list.count(obj)  # each individual item count
# Returns count of how many times obj occurs in list

# list.index(obj)
# Returns the lowest index in list that obj appears

list2 = [2,3,-33,33,4000,22]
print("len list", len(list2))

print("max =",max(list2))
print("min =",min(list2))

# Note min max function is not supported in  l = ['one',2,3,2.2] because of different type

l= ['a','d','z','b']
print(min(l))
print(max(l))

# min max function gives values which is smaller in terms of similar to a order dictionary having wordmeanign in 
# alphabetical order
la= ['abc','aac', 'dbc','zac','zaab','baa'] 
print("min=",min(la)) #prints aac because abc , aac has  a in frist but aac has a in second index
print("max=",max(la)) # prints zac because c comes after a (in zaab, third letter) from last to first

new_list = [33,44,55,2,22,11,60,-90,-66,5]

# sorting a list
new_list.sort() # sort and store in x
# note we can not do x = new_list.sort() because .sort() does not return any value it is of type None
print("sorted list=",new_list)

# reversing a list
new_list.reverse()
print("reversed list=",new_list)


'''
Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added 
is the first element retrieved (“last-in, first-out”). To add an item to the top of the 
stack, use append(). To retrieve an item from the top of the stack, use pop() without an 
explicit index. For example:
>>>
'''
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
# [3, 4, 5, 6, 7]
stack.pop()
# 7
print(stack)
# [3, 4, 5, 6]
stack.pop()
# 6
stack.pop()
# 5
print(stack)
# [3, 4]

'''
5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is 
the first element retrieved (“first-in, first-out”); however, lists are not efficient 
for this purpose. While appends and pops from the end of list are fast, doing inserts 
or pops from the beginning of a list is slow (because all of the other elements have 
to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends 
and pops from both ends. For example:
>>>
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
print(queue)                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])

# '''
