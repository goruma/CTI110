#Program will calculate a sum based on user inputed positive numbers, until user enters
#a negative number.
#3-1-2019
#CTI-110 P4HW3 - Sum of Numbers
#Adrian Gorum
#

#Pseudocode
#>Initialize a varible of user number
#>Gather input from user
#>Initialize a sum total varible
#>Use a while loop to check and see if the user inputed value is greater than 0
#>Calculate a sum total using user inputed value
#>Display sum total once while loop ends

def main():
    
    #Initialize user number variable, as well as, gather input from user on first inputed
    #positive number.
    user_num = float(input('Enter a positive number: '))
    print('')

    #Initialize total variable
    sum_total = 0

    #While loop to calculate a total + the user inputed number as long as the user doesn't
    #enter a negative number.
    while user_num > 0:
        #sum_total variable = sum_total + user_num
        sum_total += user_num

        #Continue to gather input from user
        user_num = float(input('Enter a positive number to continue(or a negative number to calculate the sum): '))
        print('')

    #Display total sum
    print('The sum of the positive numbers entered is: ', format(sum_total, '.2f'))

#Program start
main()
