# Python program that calculates tip percentages for total meal costs.
# 2-12-19
# CTI-110 P2HW2 - Meal Tip Calculator
# Adrian Gorum
#

#Pseudocode
#input total charge for meal > calculate tip percentages by multiplying total
#charge by .15, .18, & .20 > display tip amounts > calculate total cost by adding tip amount and total
#charge > display total cost based on tip amount
#

#Gather input from user on the total charge of their meal.
total_charge = float(input("Enter the total charge for meal: $"))

#Calculate the tip percentage for 15%, 18%, & 20% based on the total charge
#input by user.
tipPercentage1 = float (total_charge * .15)
tipPercentage2 = float (total_charge * .18)
tipPercentage3 = float (total_charge * .20)

#Blank print function to create a blank line.
print("")

#Display tip amount at 15%, 18%, & 20%
print("Tip amount at 15% is: $", format(tipPercentage1, ',.2f'))
print("Tip amount at 18% is: $", format(tipPercentage2, ',.2f'))
print("Tip amount at 20% is: $", format(tipPercentage3, ',.2f'))

#Blank print function to create a blank line.
print("")

#Calculate total cost of meal by adding tip percentages and total charge
#previously inputted.
total_cost1 = float (total_charge + tipPercentage1)
total_cost2 = float (total_charge + tipPercentage2)
total_cost3 = float (total_charge + tipPercentage3)

#Display total cost of meal with each tip percentage added to total charge for
#meal.
print("Total cost for a meal with a 15% tip is: $", format(total_cost1, ',.2f'))
print("Total cost for a meal with a 18% tip is: $", format(total_cost2, ',.2f'))
print("Total cost for a meal with a 20% tip is: $", format(total_cost3, ',.2f'))

