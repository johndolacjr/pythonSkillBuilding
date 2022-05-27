#SECTION 1: Getting Started w/ the Fundementals of Python Programming
# Installed Python, Pycharm, etc.

# Part 2 Basic Syntax
''''
print("Welcome to Python programming");
'''
# Part 3 commentsin Python
'''
print("This is a comment");
'''

"""
This is a multiple line comment
We have to many comments
Where are the bugs
Welcome to the world
"""

# Variables
'''
x = 15
print (x)

x = "Hello"
print(x)

# no need to specify strings etc. only assign the value to a variable
'''

""""
x = int(5)
y = float(7.9)
z = str("Name")

#Float = decimal number
# Integer or Int = whole number
# String/ str = word 
print(x)
print(y) 
print(z)

x = "Hello"
print(type(x))
# will print the class (str, float, or int) depending on the value type
# variables hold a value type - can use different names: x, X, y, Y, z, Z, val, var, age, name, etc. 
# variables are sensative - ensure lower or caps are assigned to the right values; keep it clean to avoid errors
"""

#SUB SECTION 5 - Rules of Naming variables
"""Varaibles can only contain alphanumeric(a-z), 0-9, or underscores"""
"""Variable name cant start with a number
Must start with a letter or it can start w/ an _ and can contain an _
example: namepak = 8 OR name_pak = 8 --> it will print 8

age_1 = 38
size = ("Large")
_school = ("U of U")
print (age_1, size)
print (_school)
"""

#how to assign multiple values to variables
'''
x = "pen"
y = "book"
z = "bag"

print (x)
print (y)
print (z)

#or
#Here is where we assign multiple values to variables
x, y, z = "Pen", "Book", "Bag"
print (x) 
print (y)
print (z)

x = y = z = "Book"
print (x)
print (y) 
print (z)

#Results = Book, Book, Book

School = ["Pen", "Book", "Bag"]
x, y, z = School
print (x)
print (y)
print (z)
'''

#GLOBAL VARIABLES
'''
x = "Elike"

#bringing in a function (defining our function)
def ourfunc():
    x = "Hello"
    print(x + " World")

#calling our function to run/print "Hello World"
ourfunc() 

#The function will run the local variable first and think its done
# Print this would say Hello World NOT Elike World - deleting the local variable will then cause the function to look outside of itself and then print Elike World. 

x = "Elike"

def ourfunc():
    y = "Hello"
    print ("This is a python programming" + " " + y + " " + x)

ourfunc() 
'''

#GLOBAL KEYWORD
'''
x = "Peter"

def hello():
    x = "Paul"
    print (x)
hello()

# This will print out "Paul" when run 
'''
'''
x = "Peter"

def hello():
    x = "Paul"
    print (x)
hello()

print (x)
'''
# will print out Peter as print (x) looks globally first because its not w/in the function like X="Paul"; print(x) when you call the function hello()
# how do i assign Paul to a global variable? --> Assigning a Global Keyword to X
'''
x = "Peter"

def hello():
    global x
    x = "Paul"

hello()

print (x)
'''
#Paul is printed out because it is now a global variable  --> if we do not call the function then Peter will print out

#DATA TYPES
'''
#STRINGS/ INTEGER/ FLOAT/ COMPLEX
a = "Hello World"                      #string (str) - words
b = 2                                  #integer (int) - whole numbers to infinity 
c = 3.5                                #float (float) - decimal numbers to infinity 
d = 5j                                 #complex (complex) - 

#SEQUENCE TYPES
e = ["Pen", "Paper", "Book"]           #list (list) 
f = ("Bag", "Biro", "Pencil")          #tuple (tuple) 
g = range(7)                           #range (range) 

#MARKING TYPES
i = {"Pen": "Bag", "hello" : 50}       #dictionary (dict) 

#SET TYPES:
j = {"Pen", "Bag", "Pencil"}           #set (set)
k = frozenset({"Pen", "Bag", "Book"})  #frozenset (frozenset) 

#Booleans: True or False
l = False                              #bool (boolean)
                             
#BINARY TYPES: consists of 0's and 1's 
m = b"Tree"                            #bytes (bytes)
n = bytearray(4)                       #bytearray (bytearray) 
o = memoryview(bytes(5))               #memoryview (memoryview) 

print(type(e))
'''

#CASTING - 
# Comes into play when dealing w/ numbers; you tell it to be a float, int, or string type. 
# Essentially you tell the CPU what you want the outputs to be, could be based on how you need your results.
# cant assign a string to be an int (NOT POSSIBLE); you can assign an int to be a string  
#EXAMPLES
'''
x = int(2.5)
print(x)           # will print the whole number 2 (not 2.5 b/c it is classified as an int)
print(type(x))     # will print <class 'int'>


y = float(2)
print(y)           # will print the decimal number 2.0 (not 2 b/c it is classified as a float)
print(type(y))     # will print <class 'float'>

z = str(2.5)
print(z)           # will print the decimal number 2.5
print(type(z))     # will print <class 'str'> (because you assigned it as a string)

a = int("hello")
print(a)           # will print an error because you cannot sign words to be a numerical value
print(type(a))    
'''

#SECTION 2: Strings in Python Programming 
#Introduction to Strings
#Strings are surrounded by quotation marks "Hello World"
#Strings can be assigned to a variable (x) --> print x ---> X = "Hello World"
#Multiple Strings: print
'''
x = "Hello World"
y = "multiple lines for longer text use 3 quotation marks"

#example of y = """....Lots of words....""" ---> this would carry on for multiple lines and be able to print successfully all

z = "John walked to the store to the store \
    to get a piece of candy for his kids \
    but he ate all of the candy by the time he got home"

print(z)

#backwards slash allows shorter strings to use multiple lines and print out as one string of text
'''

#String Arrays
#each letter is a character; lets print h
x = "Hello, world"

print(x[0])

#this will print the letter "h" when i run the code; the number 4 would run the leter "o"
#had to stop short...sick kids....left off at 1:41 