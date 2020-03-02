class Car:
    def __init__(self):
            print("constructor method")
    def __del__(self):
            print("destructor method")

obj_c = Car()
del obj_c


class Fruit:
    fruit_type= "orange" #public class variable
    # print("creating constructor")
    
    def __init__(self,name,f_type):
        # print("constructor")
        self.fruit_name=name
        # fruit_type is class variable which is accessed using classname.variablename
        Fruit.fruit_type = f_type # generally don't do like this

obj_fruit = Fruit("guave","summer fruit")
print(obj_fruit.fruit_name)
print(obj_fruit.fruit_type) # below is same
print(Fruit.fruit_type) # same as obj.fruit_type
