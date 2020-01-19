"""
Part1:
comments, main functions, variables, data types, type conversion

"""

'''
fjeowjfo
'''

# ----------Type conversion-------------
x = 10
y = str(x)

print(type(x))
print(type(y))
print(type(type(y)))
print(type(type(type(type(type(y))))))

a = "20"
b = int(a)
c = float(a)
after,before,longafter = 2,3,"3223few"

print(after)
print(before)
print(longafter)
print("a=",a)
print("b = ",b,type(b),a,a,a)

# ---------Print formatting---------
'''
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. 
The differences between tuples and lists are, 
the tuples cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets.
'''

country_name = "Germany"
score =3
# pass by value print statement
print("Total score for ",country_name, " is ",score)
# Using concatanation operator
print("hellow"+ str(score))

# print statement as tupal
print("Total score for %s is %s" %(country_name,score))

# print statement as dictionary
print("Total sore for {0} is {1} ".format(country_name,score))

# ----------math functions-----------
import math
print(math.ceil(2.4)) # upper value i.e. 3
print("ceil=",math.ceil(2.001)) # upper value i.e. 3
print(math.floor(2.6)) # lower value
print(math.floor(2.6)) # lower value
print("floor=",math.floor(2)) # lower value
print(type(math.ceil(2.4)))


# math.sin.__doc__
print(math.sin.__doc__)

# input value is in radian 
#  so we have to convert degree into radius as math.radian
print("from degree to radian =", math.radians(30))
print("sin(30)=",math.sin(90)) # here we mean 90 radian
print("sin(30)=",math.sin(math.radians(90))) # here we mean 90 radian

# root 2
print("sqrt=",math.sqrt(2))
# power
print("math.pow",math.pow(3,2))
print("math.pow",math.pow(3,1))
print("math.pow",math.pow(3,3))

# factorial 
print(math.factorial(4)) #24

# --------- end math function------


