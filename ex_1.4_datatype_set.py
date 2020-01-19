"""
SET: A set is an unordered collection with no duplicate elements. Basic uses include 
membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations 
like union, intersection, difference, and symmetric difference.

Set: set is an unordered immutable datatype with can contain only unique elements. 
The elements in set is immutable, however 
set in itself is mutable. 

Creation: set can be created using {} or set() method. 

Datatypes supported: It can have different datatypes memeber like int, float, tuple,string,etc. 
However, it can not have member with mutable datatype like list or dict().

Addition- .add() for single element
        - .update() for multiple element

Deletion - deletion is not supported in set using del , because indexing is not supproted

Deletion using remove()and discard():
 

Indexing - since set is unordered indexing is not supported e.g. first_set[0] is not supported

set() syntax:
set([iterable one item only])
set with list, dict - can be created using set() method but the output will be set i.e. {}
e.g set([2,33,3]) => output : {2,33,3}


"""
# --------Set creation, unordered test, unique test, indexing not supported eg.--------

# This is a valid set because to be dictionary it need to have key,value pair
first_set = {1,2,3}
print(first_set)
print(type(first_set))

# unordered test
test_set = {"one","two",2}
print("unordered test = ",test_set)

# Test of unique elements
second_set = {2,3,4,4,5,5,6}
print(second_set)
print(len(second_set)) # not 7 but 5 only counting unique elements

# test of mixed set types
third_mix_set = {1,"two",3.4, ("one",400)}
print(third_mix_set)
print(len(third_mix_set))
print(type(third_mix_set))

# elements can not be modified
# first_set[0]=4 #not allowed

# ----------------Adding item in set------------------------------------------------------

# set addition only single element using .add() method
first_set.add(4)
print("first_Set = ",first_set)

# for adding multiple element we use .update() method which can take tuple, list, string, or other datatype
first_set.update([44,55])
print("after update=",first_set)

# -------------------------Not supported: Removing item using del keyword example---------------
# removing element
# deletion not supported

# del first_set[3]
# print(first_set)

# TypeError: 'set' object doesn't support item deletion


# set with list and dict()
# fourth_set = {[],[]}
# error: TypeError: unhashable type: 'list'

# fifth_set= {dict(),{}}
# TypeError: unhashable type: 'dict'

# using tuple
sixth_set = {("one","one",2)}
print("sixth_set=",sixth_set) # prints {('one', 'one', 2)}
print(len(sixth_set))

# ----------------------Set using list and dictionary ----------------------
# set of list ([]) using set() fxn
set_with_list= set([2,33,44,2])
print("set with list=",set_with_list)

# multiple item not supported in set() method
# set_with_list= set([2,33,44,2],dict())
# TypeError: set expected at most 1 arguments, got 2

set_with_dict = set(
    {
        "p1":1,
        "p2":2,
        "p3":3,

    }
)

# output only key which is converted to key values
print("set with dict=",set_with_dict)

set_with_dict2 = set(
    {
        "p1":1,
        "p2":2,
        "p3":3,
        "p1":33

    }
)
# repeted item is removed
print("set with repeted item=",set_with_dict2)

# set of set
set_of_set = set({2,3,4,4,4})
print("set of set=",set_of_set) # prints {2,3,4}

# set with string ,note each element in string is iteriable
a = set("one") # converts string into set items
print("a=",a) # prints {'o', 'n', 'e'}

# iteriable test this gives error 

# b = set(33333)

# TypeError: 'int' object is not iterable
# ----------------------------Removing item form set--------------------------
# Removing item from set
# using discard() method: it removes item if the item is not present it does not give error.
set_example = {1,2,3,4}
# remove using discard
set_example.discard(4) # remove four
print("set example=", set_example)

# discard unavailable item
set_example.discard(44)

# removing item using remove it raises error if item is not present
set_example.remove(3)
print("set_example after remove= ", set_example)

# lets remove unavailable item
# set_example.remove(44) # should raise exception

# --------------------Set operation union, intersection,  difference--------------

# union using | and .union() function
a = {1,2,3,4,5}
b = {4,5,6,7,8}

u = a | b 
print("union of a ,b =", u)

u = a.union(b) 
print("union of a ,b =", u)

# intersection using & and .intersection() function
i = a & b 
print("intersection = ",i) 

i = a.intersection(b) 
print("intersection = ",i) 

# difference using minus(-) and .difference() method
d = a - b 
print("difference d =",d)

d = a.difference(b) 
print("difference d =",d)
