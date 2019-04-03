# Program generates a random number between 1 & 100, and asks the user to guess what the number is. If the user's guess
# is higher or lower than the random number the program continues to ask the user for input. If the user guesses the
# random number the program congratulates the user and asks if the user wants to play again. 
# 4-3-2019
# CTI-110 P5HW1 - Random Number
# Adrian Gorum
#

#Psuedocode
#>Import random module
#>Initialize global variables for random range and user attempts
#>Define main() function
#>Display information to user of what the program does inside main() function
#>Initialize variable for a random number inside main() function
#>Define ranLoop() function with two arguments
#>Prompt user to enter a whole number and store user input as local variable
#>Perform a while loop to determine whether user input is greater than, less than, or equal to the random number variable
#>Calculate the accumulation of user's attempts
#>Display results to user if random number equals user input
#>Call ranLoop() function and pass aiNum argument and guess_attempt argument
#>Define a playAgain() function
#>playAgain() function prompts user to input Y or N to decide whether to run the program again
#>Determine if player has inputted Y or N
#>Prompt user for input if player inputs Y
#>Call ranLoop() function again if user inputs Y
#>Call exit() function to terminate program if user inputs N

#Imports random module
import random

#Initialize Global Variables
MINNUM = 1
MAXNUM = 100
guess_attempt = 1

#main() function informs user about the program and generates the first random number. Calls ranLoop() function to start the game.
def main ():
    #Inform user of what the program does.
    print("This program generates a random number between 1 and 100. \nAttempt to guess the random number!\n") 

    #Generate first random number.
    aiNum = random.randint(MINNUM, MAXNUM)

    #Calls ranLoop() function and passes first random number and guess attempt as arguments.
    ranLoop(aiNum,guess_attempt)

#ranLoop() function prompts user to enter their guess and stores this value in user_guess variable. The performs a
#while loop to continue prompting the user for a whole number until the random number is guessed. Once random number
#is guessed this function calls the playAgain() function.
def ranLoop (aiNum,guess_attempt):
    #Promt the user for whole number and stored as int type in user_guess variable
    user_guess = int(input("Enter a whole number between 1 & 100: ",))
    print('')

    #while loop continues to prompt user for a whole number to store in user_guess variable as long as the user_guess
    #is greater than or less than the random number generated.
    while aiNum > user_guess or aiNum < user_guess:
        #Determine if user_guess is 'too high' or 'too low' compared to the random number. Prompt user to try again.
        if user_guess > aiNum:
            print("Too high! Try again!\n")
            #Promt the user for whole number and stored as int type in user_guess variable.
            user_guess = int(input("Enter a whole number between 1 & 100 again: "))
            print('')
        elif user_guess < aiNum:
            print("Too low! Try again!\n")
            #Promt the user for whole number and stored as int type in user_guess variable.
            user_guess = int(input("Enter a whole number between 1 & 100 again: "))
            print('')
            
        #guess_attempt variable accumulates by 1 on every iteration of while loop
        guess_attempt += 1

    #if statement checks if the random number is equal to the user_guess variable and displays the results if true.
    if aiNum == user_guess:
        print("Congratulations! The random number was:",aiNum,"\n")
        print("You guessed the random number in only",guess_attempt,"attempts!!!!!\n")
        print("You WIN!!!!\n")
        #Calls playAgain() function
        playAgain()
    #else:
        #Intentionally left blank. Do not have an else clause but was marked off points previously for missing
        #an "else" when not needed.

#playAgain() function prompts the user to decide if they want to play the guessing game again. If the user chooses yes
#the program restarts. If the user chooses no the program exits.
def playAgain():
    #Prompt the user to choose whether to play again. Gather input as string.
    playChoice = input("Would you like to play again? Y or N: ")
    print('')

    #Determine whether user has chosen to play again or not using an if/else statement
    if playChoice == 'y' or playChoice == 'Y':
        #Inform the user that the program is starting again and that a new random number has been generated.
        print("Lets play again! A new random number has been generated between 1 and 100. \nAttempt to guess the random number!\n")
        #Generates new random number.
        aiNum = random.randint(MINNUM, MAXNUM)
        #Calls ranLoop() function 
        ranLoop(aiNum,guess_attempt)
    #if player chooses not to play again program will exit.
    elif playChoice == 'n' or playChoice == 'N':
        exit()
    

main()

    
