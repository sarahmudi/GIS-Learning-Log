print("Hello, World!")

#Syntax matters
if 5>2:
    print("Five is greater than two!")

#Python Variables
x = 5
y = "Hello world!"   
z = 2
if x > z:
    print(y)

#Variable names
#Must start with a letter or underscore and cannot start with a number; can only contain A-Z, 0-9, and _
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John" 
myvar2 = "John" 

print(type(_my_var))
print(type(MYVAR))

#Assign multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print( x, y, z)
print(x)
print(y)
print(z)

x = y = z = "Amazing"
print (x)
print (y)
print (z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print (x, y, z)

#Output Variables
X = "Python is awesome!"
x = "Python"
y = "is"
z = "awesome!"
print (X)
print (x, y, z)
print (z, y, x)
print (x + y + z) # no spaces
print (5 + 10) # for int, it will act as a mathematical operator
# you cannot use + when using a str and an in
a = 5
print (x, a)


#Global variables
#variables created outside of a function are known as global variables as they can be used by functions or outside
x = "awesome"
def myfunc():
    print ("Python is " + x)

myfunc()

def myfunc():
    x = "fantastic"
    print ("Python is " + x)

myfunc()

print ("Python is " + x)


#Built in Data Types
#Test Type : str
#Numeric Type : int, float, complex
#Sequence Type: list, tuple, range
#Mapping Type: dict
#Set types: set, frozenset
#Boolean Type: bool
#Binary Types: bytes, bytearray, memoryview
#None Type: NoneType

x = 5
print(type(x))

#set the data type
x = "Hello World" #str
print(type(x))

x = 20	#20
print(type(x))

x = 20.5 #float
print(type(x))

x = 1j #complex
print(type(x))

x = ["apple", "banana", "cherry"]	#list
print(type(x))

x = ("apple", "banana", "cherry")	#tuple
print(type(x))

x = range(6)	#range
print(type(x))

x = {"name" : "John", "age" : 36}	#dict
print(type(x))

x = {"apple", "banana", "cherry"}	#set
print(type(x))

x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(x))

x = True	#bool
print(type(x))

x = b"Hello" #bytes
print(type(x))

x = bytearray(5)	#bytearray
print(type(x))

x = memoryview(bytes(5))	#memoryview
print(type(x))

x = None #NoneType
print(type(x))

#Python casting-Specify a variable type
x = 12.1 + 12
print(type(x))

print(x)
print(int(x))
print(float(x))
print(str(x))


