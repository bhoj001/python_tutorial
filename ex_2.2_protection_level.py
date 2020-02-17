# Public class variables
class Car:
    door_number=4 # Public class variable
    def get_color(self): # public method
        return "Blue"

obj = Car()
print(obj.door_number)
print(obj.get_color())


# Protected and private:
"""
We use convention here:
we use single underscore as _variableName, to make protected memeber
We use double underscore as __variableName to make it private.  
"""
# Protected example
"""
Python's convention to make an instance variable protected is to add a 
prefix _ (single underscore) to it. 
This effectively prevents it to be accessed, unless it is from within a sub-class.

Is accessible from object of class and object of subclass or subclass members

But it can not be accessible using `classname.variable` name 
"""
class employee:
    def __init__(self, name, sal):
        self._name=name  # protected attribute 
        self._salary=sal # protected attribute
        self._company = "Google Inc."

e1=employee("Swati", 10000)
print(e1._salary)
# ----we can not do this because we have to define _name using constructor. 
# print(employee._name)
# AttributeError: type object 'employee' has no attribute '_company'
# print(employee._company)



# Private variable: only accessible inside class
# can not access outside the class or via an object
class employee2:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute
        self.__company="google inc"

    # this one is public method
    def display_company(self):
        # can do like self.__company inside the class
        print("company=",self.__company)


e1=employee2("Bill",10000)
# -------- cant do like this
# print(e1.__salary) #AttributeError: 'employee2' object has no attribute '__salary'
# print(e1.__company) # does not work

# ----- Can't do
# print(employee2.__company)
# print(employee2.display_company()) #TypeError: display_company() missing 1 required positional argument: 'self'


# -------can do
e1.display_company()

# However we can use name mangeling technique if we really want to access it
print(e1._employee2__company)
