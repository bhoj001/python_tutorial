# Normal function without return type
def name():
    print("I am ram")
    

def custom():
    print("custom department")
    return True

name()
custom()

# function with parameter
def coordinate(x,y):
    print("coordinate =(",x,",",y,")")

coordinate(20,30)

def circle_center(x=0,y=0):
    print("circle center =(",x,",",y,")")

circle_center()
circle_center(3,4)
# enforcing parameter type
def enforce_parameter(x):
    if not isinstance(x,int):
        raise TypeError
    print("x is an integer, value= ",x)    

enforce_parameter(3)
# enforce_parameter("String") # raise error