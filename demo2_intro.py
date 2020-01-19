''''
# Comment in python,variables
0. different print statement
1. Numbers
2. Strings
3. List
4. dictionaries
5. conditional loops
'''

# single line comment
'''
This is a multi line comment
'''
"""
This is another way of multiline comment
"""
# simple print
print("This is a simple printed text!")

# variables 
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

#Numbers in python
print("Add=",12+34)
print("Subtract=",12-34)
print("Multiply=",12*34)
print("Divide=",12/34)
print("Remainder=",5%2)

height = 22
breadth = 12
lenght = 10
volume =lenght*breadth*height
print("volume=",volume)
# strings , indexing starts with 0
words = "Nishant karki"
print(words)
print(words[0])
print(words[1])
print(words[-1])
print(words[3:])
print(words[3:8])
# Escaping special characters
print('C\something\name')
print(r'C:\something\name')

print("""\
 hi i'm nishant karki
 and i am teaching you python programming

""")

# list in python
# add into a list
# remove from list 
ls = [1,2,3,4,5]
print(ls)

# add to a list 
ls.append(6)
ls.append(7)
print("new list=",ls)
ls.insert(0,-4)
print("new inserted list=",ls)
ls.remove(-4)
print("list after remove=",ls)

# Dictionaries in python
phonebook ={} # empty dictionary
phonebook["mike"]=8889834983489
phonebook["jack"]=2229834900000
phonebook["james"]=989989834999489

print(phonebook)

phonebook={
    "mike":9834983489,
    "jack":9834900000,
    "james":9834999489
}

phonebook["john"]=9845669909
print("new phonebook=",phonebook)

#deleting from dictionary
del phonebook["mike"]

phonebook.pop("jack")

print("new value in dictionary=",phonebook)


#Conditional statements if elif..
country1="Gernamy"
score1 = 2
country2 = "united kingdom"
score2 =2

if score2> score1:
    print("{} is the winner".format(country2))
elif(score2<score1):
    print("{} is the winner".format(country1))

else:
    print("equal score!")


