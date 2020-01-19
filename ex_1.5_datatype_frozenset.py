'''
author: bhoj bahadur karki
date: 2020-jan-19th
purpose : about frozenset in python

set vs frozenset:

There are currently two built-in set types, set and frozenset. The set type is mutable — the 
contents can be changed using methods like add() and remove(). Since it is mutable, 
it has no hash value and cannot be used as either a dictionary key or as an element 
of another set. The frozenset type is immutable and hashable — its contents cannot 
be altered after it is created; it can therefore be used as a dictionary key or as 
an element of another set.

Both set and frozenset support set to set comparisons. Two sets are equal if and only if every 
element of each set is contained in the other (each is a subset of the other). A set is less 
than another set if and only if the first set is a proper subset of the second set (is a subset, 
but is not equal). A set is greater than another set if and only if the first set is a proper 
superset of the second set (is a superset, but is not equal).

Instances of set are compared to instances of frozenset based on their members. 
For example, set('abc') == frozenset('abc') returns True and so 
does set('abc') in set([frozenset('abc')]).
'''

x = frozenset([2,3,4])
print(x)
# x[0]=3 # TypeError: 'frozenset' object does not support item assignment

# x.clear() # AttributeError: 'frozenset' object has no attribute 'clear'

# -----Methods supported by set but not frozenset-------
'''
The following table lists operations available for set that do not apply to immutable instances 
of frozenset:

update(*others)
set |= other | ...

    Update the set, adding elements from all others.

intersection_update(*others)
set &= other & ...

    Update the set, keeping only elements found in it and all others.

difference_update(*others)
set -= other | ...

    Update the set, removing elements found in others.

symmetric_difference_update(other)
set ^= other

    Update the set, keeping only elements found in either set, but not in both.

add(elem)

    Add element elem to the set.

remove(elem)

    Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)

    Remove element elem from the set if it is present.

pop()

    Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

clear()

    Remove all elements from the set.

'''

