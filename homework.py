
"""
Exercise 1:
1. Create a fibonachi sequence using python for n values i.e 
input = maximum value 
output= sequence
e.g. 0, 1 , 1, 2, 3, 5, 
"""
def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)

# """

'''
For basics:
Exercise 2:  User Input [This is optional]
Write a Python program to print the output of multiplication of three numbers 
which will be entered by the user.
Test Data:
Input the first number to multiply: 2
Input the second number to multiply: 3
Input the third number to multiply: 6
Expected Output:
2 x 3 x 6 = 36
'''

'''
Exercise 3: input from keyboard(user input)
Write a Python program to that takes three numbers(x,y,z) as input and print the output of 
1. (x+y).z and 
2. x.y + y.z. 

Test Data:
Enter first number - 5
Enter second number - 6
Enter third number - 7
'''

'''
Exercise 4: input from keyboard
Write a Python program that takes the radius of a circle as input and calculate 
the perimeter and area of the circle.

Test Data
Input the radius of the circle :
12
Expected Output :
Perimeter of Circle : 75.36
'''

'''
Exercise5:  conditional statement
Write a Python program to read the age of a candidate and determine whether it is 
eligible for casting his/her own vote.

Test Data : 21
Expected Output:
Congratulation! You are eligible for casting your vote
'''
'''
Exercise 6: Loops
Write a Python program to find the sum of first 10 natural numbers. Go to the editor
Expected Output :
The first 10 natural number is :
1 2 3 4 5 6 7 8 9 10
The Sum is : 55
'''

'''
Exercise 7. Array/List - difficulty - easy

Write a program in Python to count a total number of duplicate elements in an array.
Test Data :
Input the number of elements to be stored in the array :3
Input 3 elements in the array :
element - 0 : 5
element - 1 : 1
element - 2 : 1
Expected Output :
Total number of duplicate elements found in the array is : 1
'''
# note ->int means it return int value
# from typing import List
# forcing parameters
# def arr_duplicate(ar:List)->int:
def arr_duplicate(ar):
    print('ar=', ar)
    count = 0
    x = set(ar)
    
    if len(x)==len(ar):
        return 0
    for item in x:
        a = item
        number = 0
        for val in ar:
            if a == val:
                number +=1
                if number > 1:
                    count+=1
                    break 
    return count

# a = [2,2,3,3,3,3,4,5]
# print("count = ",arr_duplicate(a))

# b = [2,5]
# print("count = ",arr_duplicate(b))

# c = [2,2,3,3,3,3,4,4,5,5]
# print("count = ",arr_duplicate(c))

# d = []
# print("empty count =",arr_duplicate(d))

# e = {2,3,4,5,5} # will be represented as {2,3,4,5} automatically so always zero in count
# print(type(e))
# print("empty count =",arr_duplicate(e))


'''
Exercise 8: Function example
4. Write a program in Python to create a function to input a string and count number 
of spaces are in the string.
Test Data :
Please input a string : This is a test string.
Expected Output :
"This is a test string." contains 4 spaces
'''
