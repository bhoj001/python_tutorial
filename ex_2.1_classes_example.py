class Car:
    door_number = 4
    engine = "petrol engine"
    color = "blue"

obj = Car()
print(obj.door_number)

'''
Class variable/attribute=  A variable that is shared by all instances of a class. 
            Class variables are defined within a class but outside any of the class's methods

Instance variable − A variable that is defined inside a method and belongs only to 
            the current instance of a class.
'''



class Person:
    count=0 #class attribute

    def __init__(self): #constructor
        self.name= "ram" #instance attribute
        self.age= 8 #instance attribute

    def displayInfo(self): #method
        print(self.name, self.age)

t = Person()
t.displayInfo()

# print(t.count)
# t.count = 4
# print(t.count)

# y = Person()
# print(y.count)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        # empCount += 1 # we can not access it like this it will show error 
        # UnboundLocalError: local variable 'empCount' referenced before assignment

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

# "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

'''
The variable empCount is a class variable whose value is shared among all instances 
of a this class. This can be accessed 
as Employee.empCount from inside the class or outside the class.

The first method __init__() is a special method, which is called class 
constructor or initialization method that Python calls when you 
create a new instance of this class.

'''

