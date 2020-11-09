

#Trip Cost calculation
miles = int(input("How many miles are you going drive? "))
mpg = int(input("How many miles per gallon does your vehicle get? "))
price = float(input("What's the price of gas? "))

gallonsUsed = miles // mpg
gasCost = price * gallonsUsed
print("That leaves your trip costing you ", gasCost, " immediately in fuel.")
print("Have a blessed day")

#Convert Inches to Centimeters

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : " % h_cm)


# Body Mass Index:-

height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))
