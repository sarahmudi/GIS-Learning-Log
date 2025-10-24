#Conditional (if/else):
# if condition:
#    do this
# else:
#    do this

water_level = 50
if water_level > 80:
    print("Drain water!")
else:
    print("Continue")


#control flow example
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))

if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry! You have to grow a little taller before you can ride.")


#Check for odd or even
number = int(input("What is the number? (Whole numbers only!)"))
check_remainder = number%2
if check_remainder == 0:
    print("Number is even")
else:
    print("Number is odd")

#Nested if example
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))

if height > 120:
    print("You can ride the roller coaster!")
    if age <= 18:
        print("It will be $7!")
    else:
        print("It will be $12!")
else:
    print("Sorry! You have to grow a little taller before you can ride.")

#Elif example
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))

if height > 120:
    print("You can ride the roller coaster!")
    if age <= 18:
        print("It will be $7!")
    elif age <= 12:
        print("It will be $5!")
    else:
        print("It will be $12!")
else:
    print("Sorry! You have to grow a little taller before you can ride.")

#Revamped BMI Calculator
weight = int(input("What is your weight?"))
height = int(input("What is your height?"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi > 25:
    print("overweight")
else:
    print("normal weight")

#Multiple If Statements
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
picture = input("Do you want a picture? Put Y for yes and N for no.")

if height > 120:
    print("You can ride the roller coaster!")
    if age <= 18:
        price = int(7)
    elif age <= 12:
        price = int(5)
    else:
        price = int(12)
    if picture == "Y":
    price = price + 3
    else:
    price = price

    print("Your total is $" + str(price))
else:
    print("Sorry! You have to grow a little taller before you can ride.")

#Pizza Order Practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")
total = 0

if size == "S":
    total = 15
    if pepperoni == "Y":
        total += 2
    else:
        total = price
elif size == "M":
    total = 20
    if pepperoni == "Y":
        total += 3
    else:
        total = price
elif size == "L":
    total = 25
    if pepperoni == "Y":
        total += 3
    else:
        total = price
else: 
    print("Sorry, incorrect entry! Try again!")

if extra_cheese == "Y":
    total += 1
else:
    total = price

print("Your total is $" + str(total))

