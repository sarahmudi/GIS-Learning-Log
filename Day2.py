# Data Types: String, Integer, Float, Boolean


#Strings ("string of characters")
# Substripcting
print("Hello"[4]) #starts at 0 and from the first character

print("Hello"[-1]) #starts from the last character

#Concactonation
print("123" + "456")


#Integers are whole numbers
print(123+345)

#Large Integers
print(123_456_789)

#Float= Floating Point Number or decimals
print(3.14159)

#Boolean (True or False)
print(True)
print(False)


#BMI Calculator
height = input("What is your height? (In meters)")
weight = input("What is your weight? (in kilos)")

bmi = weight // (height * height)

print (bmi)