'''
AUTHOR:Bhoj Bahadur Karki
Purpose: Teaching file operation

Topics:
How to Create a Text File
How to Append Data to a File
How to Read a File
How to Read a File line by line
File Modes in Python
'''
# File modes
'''
Mode	Description
'r'	    Open a file for reading. (default)
'w'	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	    Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	    Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	    Open in text mode. (default)
'b'	    Open in binary mode.
'+'	    Open a file for updating (reading and writing)
'''

# Opening a file 
# f = open('human.txt','w+')

'''
Different modes

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

Unlike other languages, the character 'a' does not imply the number 97 until 
it is encoded using ASCII (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, 
it is 'cp1252' but 'utf-8' in Linux.

So, we must not also rely on the default encoding or 
else our code will behave differently in different platforms.

Hence, when working with files in text mode, 
it is highly recommended to specify the encoding type.

f = open("test.txt",mode = 'r',encoding = 'utf-8')

'''

# ------File closing---
# f = open("test.txt",encoding = 'utf-8')
# # perform file operations
# f.close()

# Simple file creation 
f = open("human.txt","w+")

f.close()


# Writing to a file
'''
f.write("string to write") syntax

'''

 
f = open("human.txt","w+")
# This line will over write any content in human.txt file
for i in range(10):
    f.write("This is line number {0}\n".format(i+1))
f.close()
# appending to a file

f = open("human.txt","a") # a opens file in append mode
f.write("This is line number 100")
f.close()
# Reagind file using f.read() function 
'''
We can use the read(size) method to read in size number of data. 
If size parameter is not specified, it reads and returns up to the end of the file.
f.read(size), if size is not given then reads to end of file
'''
f = open("human.txt","r")
print(f.read()) # 

f.close()

# reading by size

f = open("human.txt","r")
print(f.read(4)) #prints first 4 bytes i.e.: 'This'
print(f.read(4)) # next four data.ie. {space}is{space}

f.close()

# Reading line by line
'''
For reading line by line we can use two ways:
1. for loop e.g for line in f:
2. using f.readline() function
'''

f = open("human.txt", mode="r",encoding='utf-8')
for ln,line in enumerate(f):
    print("Line: ",ln,line)
    # ln start index in 0 so 4 means fifth line
    if ln == 4:
        print("---------------------")
f.close()

# using readline() function
f = open("human.txt","r")
print(f.readline()) # reads single line
f.close()

# using 'with' in open() function
# with keyword helps to automatically close file. It makes sure even if there is exception resources is 
# freed properly
# with helps to close file automatically and free resources, if there is exception we can use with 
# to confirm that resource is freed properly
print("-----with and open() example---------")
with open('human.txt',mode="r",encoding='utf-8') as f:
    for line in f:
        print(line) 

# This should work perfectly fine
f = open("human.txt","r")
print(f.readline()) # reads single line
f.c-lose()