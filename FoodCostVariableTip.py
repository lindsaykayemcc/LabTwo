#Input List
foodcost = 0.0
tip = 0.0
tax = 0.0
total = 0.0

#input
foodcost=float(input("What is the food cost?:"))

if foodcost < 5.99:
    tip = float(0.10)
else:
    5.99 <foodcost < 12.01,
    tip = float(0.15)

if 12.00 < foodcost < 17.01:
    tip = float(0.20)
else:
    17.00 < foodcost < 25.00,
    tip = float(0.25)

if foodcost > 25.01:
    tip = float(0.30)

tax = float(0.10)

total = foodcost + (foodcost * tip) + (foodcost * tax)

print ("your food total is ", foodcost)
print ("Your tax total is ", (tax * foodcost))
print ("Your tip total is ", (tip * foodcost))
print("Your total is ", total)