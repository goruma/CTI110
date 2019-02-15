# CTI-110 
# P3HW2 - MealTipTax 
# Adrian Gorum
# 2-15-19
#

#Pseudocode
#Gather input from user for meal_charge > Gather input from user for what percentage to use; 15%, 18%, or 20%
#> Perform check for whether user enters the wrong percentage value > Calculate tip_pecent, sales_tax, & total_cost >
#Display tip_percent, sales_tax, & total_cost

#Gather input from user for meal charge.
meal_charge = float(input("What is the charge for your meal? $"))
print("")

#Gather input from user for which tip percentage they'd like to use.
tip_choice = int(input("What tip percentage would you like to use: 15, 18, or 20? "))
print("")

#Determine whether tip choice input is 15, 18, or 20
if (tip_choice == 15) or (tip_choice == 18) or (tip_choice == 20):
    print("Your tip choice is: ",tip_choice,"%")
    print("")
else:
    print("ERROR: WRONG TIP PERCENTAGE ENTERED!!!")
    print("")
    tip_choice = int(input("Please enter the tip percentage you'd like to use: 15, 18, or 20. "))
    print("")
    if (tip_choice == 15) or (tip_choice == 18) or (tip_choice == 20):
        print("Your tip choice is: ",tip_choice,"%")
        print("")
    else:
        print("CRITICAL ERROR: RESTART PROGRAM")
        exit()
    
#Initiated tip percent variable
tip_percent = float(0)

#Determind tip percent
if tip_choice == 15:
    tip_percent = float(.15)
elif tip_choice == 18:
    tip_percent = float(.18)
elif tip_choice == 20:
    tip_percent = float(.20)

#Calculate tip amount
tip_amount = float(tip_percent * meal_charge)

#Calculate sales tax
sales_tax = float(meal_charge * .07)

#Calculate total cost
total_cost = float(meal_charge + sales_tax + tip_amount)

#Display Tip Amount, Sales tax, and Total Cost
print("Tip: $",format(tip_amount, ',.2f'))
print("Sales Tax: $",format(sales_tax, ',.2f'))
print("Total Cost: $",format(total_cost, ',.2f'))
print("")

restart = input("PRESS ENTER TO EXIT.")



    
