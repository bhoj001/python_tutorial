# This function adds two numbers
def add(x, y):
   return x + y

# This function subtracts two numbers
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   if y == 0:
      return "Divide by zero error"
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user

choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
   print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
   print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
   print(num1, "/", num2, "=", divide(num1, num2))
else:
   print("Invalid input")



"""
comment here for
multi-line
comment
"""
print("hi from python")
# single line comment

var = 300
integer_variable = 1
string_varaible = "hellow universe"
float_variable = 3.14

def my_function():
   print("Inside of a funtion")

# string datatype
s= "pythonspark" 
#is an integer datatype
x = 3 
#float data type having floating point value
y = 1.2 
# complex data type
z = 3+1.2j  # we can also do, z = complex(3+1.2j)
# list datatype
a = ["1",2,"one",1.3] 
# tuple datatype
b = tuple(("fruit","vegetable","juice")) 
# range datatype, it gives range between (0 and 3)i.e. 0,1,2 for this case
c = range(3)
# below is dictionary data type
# dictionary is defined with {key:value,....} 
d = {
   "player_name": "pythonspark",
   "score": 100,
}
# set datatype
e =  set(("grapes","mango","orange"))
# boolean datatype
# defines a true value, we can also use 0 OR 1 in place of True and false
#  for e.g. f = bool(1)
f = True 
g = False # or g = bool(0)
# bytes datatype
h = bytes(4)
# bytearray datatye
i = bytearray(4)
# memoryview datatype
x = memoryview(bytes(5))


a= "python "
b = "spark"
c = a+b # this will give python spark in variable c

s = "pythonspark"
a = s[0:6]
s[-5:]
s = "pythonspark"
s.upper() # this will give "PYTHONSPARK" in upper case value

s = "pythonspark"
len(s)

val1 = 5
if val1 == 1:
   print("value one")
else:
   print("not value one")

# if condition1:
#    # if block
# elif condtion2:
#    # block 2
# elif condition3:
#    #  block 3.. 
# else:
#    ..... and so on


age = 20 
if age < 13:
   print("child")
elif age > 12 and age <= 19:
   print("Teen")
elif age > 19 and age <50:
   print("adult person")
else:
   print("old person")       
       

fruits = ["mango","orange","apple","grape"]
for item in fruits:
   print(item) # just print the name of fruits
else:
   print("completed loop")

fruits = ["mango","orange","apple","grape"]
count = 0
while(True):
   print(fruits[count])
   count+=1
   if count > 3:
      break

