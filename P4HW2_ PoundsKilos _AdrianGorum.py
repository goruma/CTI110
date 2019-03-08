#This program converts pounds to kilograms using a for loop with a starting lb
#value and an ending lb value with an increment of 10. Then displays a table of
#lbs to kgs.
#3-1-2019
#CTI-110 P4HW2 - Pounds to Kilos Table
#Adrian Gorum
#

#Psuedocode
#>Initialize variables from starting pound and ending pound value
#>Display a title for pounds to kilogram table
#>Use a for loop to display table of converted pounds to kilograms using a range


def main():
    
    #Initialize pound variabls
    starting_lbs = 100
    ending_lbs = 301

    #Display table title
    print('Pounds\tKilograms')
    print('-----------------')
    print('')

    #For loop to display table of lbs converted to kgs in range from 100 to 300 
    #with an increment of 10
    for lbs in range(starting_lbs, ending_lbs, 10):
        #convert lbs to kgs and initialize kg varible
        kg = lbs/2.2046
        #display lbs to kgs table
        print(lbs, '\t', format(kg, '.1f'))

#Program start
main()
