# say about pass
""" 
List:
1. __str__ : makes 
2. __doc__ : prints the documentation of a class
3. __len__
4. __call__ : makes object callable
5. __getitem__: Called to implement evaluation of self[key]. 
                For sequence types, the accepted keys should be integers and slice objects 
6. __repr__: 

"""

# __str__ example
"""
__str__() is used to handle you get the see the friendly name of the object.
"""

class Person:
    pass

obj = Person()
print(obj)  # prints memory location

# Class with __str__ implemented
class Person1:

    def __str__(self):
        return "Friendly object name"

p = Person1()
print(p) # prints: Friendly object name

# ---------------------------------------

# __doc__:  provides a documentation of the object. 

class Fruit:
    """ 
    Collection of fruits
    """
    pass


x = Fruit()
print(x)  # prints object location
print(x.__doc__) # prints fruit documentation, if there is no documentation if prints None

#--------------------------------------
# __len__: defines how len() function behaves
class Circle:
     def __init__(self, radius1, radius2):
         self.radius1 = radius1
         self.radius2 = radius2

     def __len__(self):
         return 2   # this should be integer


c = Circle(5,6)

print(len(c)) # prints area pi * r^2

# -------------------------------------
# __repr___:  should return a printable representation of the object, 
# most likely one of the ways possible to create this object. 
#  __repr__ is more for developers while __str__ is for end users.

class Point:    
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

p = Point(1, 2)
print(p)

# ------------------------------
# __call__: __call__
# You can make an object callable like a regular function by adding the __call__ dunder method. 

class SomeClass:
    
    def __call__(self):
        return "Object is called!!!"

obj = SomeClass()

print( obj() )