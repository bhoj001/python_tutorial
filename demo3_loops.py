'''
Loops and functions and import statements

'''
import math

print("value of sin(35)=",math.sin(35))

ls = [1,3,5,"hellow",5.4]

for value in ls:
    print(value)

initial=1
while initial < 6:
    print(initial)
    initial += 1 # initial = initial + 1  

letters = "Python Fun"
for letter in letters:
    if letter == 't':
        continue 
    print("letter=",letter)


# Functions 
'''
def fxn_name(p1,p2,..):
    ...
    ...
'''
def my_custom_function(start, end,step):
    while start <= end:
        yield start
        start += step

for x in my_custom_function(5,25,0.75):
    print("x=",x)


print("value of sin(35)=",math.sin(35))

#4! = 4*3*2*1
print("factorial of 4=",math.factorial(4))
