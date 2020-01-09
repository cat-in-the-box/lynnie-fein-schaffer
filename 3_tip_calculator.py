total_bill = float(input("How much was the total cost of the meal?"))
tip_percent = (float(input("What percentage would you like to tip?"))*.01)
print(str("Your total bill is $") +str((total_bill*tip_percent)+total_bill))