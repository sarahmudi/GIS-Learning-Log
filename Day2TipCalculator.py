print("Welcome to the Tip Calculator!")
TotalBill = float(input("What was the total bill amount?"))
TipPercentage = float(input("How much tip would you like to give? 10, 12, or 15?"))
TotalPeople = float(input("How many people to split the bill?"))

PerPerson = str(((TotalBill * (TipPercentage / 100)) + TotalBill) / TotalPeople)

print("Each person should pay: $" + PerPerson)