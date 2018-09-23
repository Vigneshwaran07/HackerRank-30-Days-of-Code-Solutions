mealcost = float(input())
tip = int(input())
tax = int(input())

tipcost = mealcost*(tip/100)
taxcost = mealcost*(tax/100)
total = round( mealcost + tipcost + taxcost )

print(total)
