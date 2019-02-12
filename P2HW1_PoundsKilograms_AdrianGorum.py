# Program converts pounds value to kilograms for users. 
# 2-12-2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Adrian Gorum
#

#Pseudocode
#input pound amount > calculate pound amount divided by 2.2046 > display
#conversion in kilograms

#Get user input for pound amount.
poundAmount = float(input('Enter the pound amount to be converted: '))

#Calculate the kilogram amount as pound amount / 2.2046.
kilogramAmount = poundAmount / 2.2046

#Display the pound amount as kilograms.
print('The pound amount converted to kilograms is: ', format(kilogramAmount, ',.3f'))
