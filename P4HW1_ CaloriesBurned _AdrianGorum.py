#Program calculates calories burned. 5 calories a minutes for 20 minutes,
#35 minutes, & 45 minutes.
#3-1-2019
#CTI-110 P4HW1 - CaloriesBurned
#Adrian Gorum
#

#Psuedocode
#>Initialize a burn rate variable
#>Use a for loop to caclulate 3 interations for 20 mins, 35 mins, & 45 mins
#>Display results of for loop

def main():
    
    #Initialize burn rate variable
    burn_rate = 5

    #For loop to calculate and display caloried burned in 3 iterations
    for minutes in (20, 35, 45):
        print('Calories burned in' ,minutes, 'minutes:', minutes*burn_rate, 'calories')

#Program start
main()
