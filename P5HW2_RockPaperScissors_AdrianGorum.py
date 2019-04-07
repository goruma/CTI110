# This program allows the user to play rock, paper, scissors with the computer. 
# 4-4-2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Adrian Gorum
#

#Imports random Module
import random

#Initialize Global Variables
#Initialize minimum and maximum variables for a range to pick random numbers from.
MIN = 1
MAX = 3
#Also initializes gameRestarts variable for determining how many times the game has been restarted
gameRestarts = 0

#Define main() fucntion which prints a different message to the user based on gameRestarts global variable, 
#initializes the aiRandom variable which chooses between a range of MIN and MAX, and calls the other defined
#functions to play the game.
def main(gameRestarts):
    
    if gameRestarts == 0:
        print("LET'S PLAY ROCK, PAPER, SCISSORS HUMAN!!!\n")
    elif gameRestarts > 0:
        print("LET'S PLAY AGAIN!!!\n")
    
    #Initialize aiRandom variable to store a random int between MIN and MAX
    aiRandom = random.randint(MIN,MAX)

    #Initialize aiPick variable storing which decision is picked by the computer based on aiRandom variable
    aiPick = aiDecision(aiRandom)
    #Initialize playerPick variable which stores the returned value from playerDecision() function    playerPick = playerDecision()

    #Calls calculateChoices() function and passes aiPick and playerPick as arguments
    calculateChoices(aiPick,playerPick)
    #Calls restart() function and passes gameRestarts variable as an argument.
    restart(gameRestarts)    


#Define aiDecision() function which requires aiRandom argument. This function determines which random #number, between MIN and MAX is assigned to aiRandom and assigns either rockm, paper, or scissor string to #the aiChoice variable.
def aiDecision(aiRandom):
    #Initialize aiChoice variable
    aiChoice = "str"

    #Determine which string to assign to aiChoice variable based on the random int assigned to aiRandom
    if aiRandom == 1:
        aiChoice = "rock"
    elif aiRandom == 2:
        aiChoice = "paper"
    elif aiRandom == 3:
        aiChoice = "scissors"
    #return aiChoice variable
    return aiChoice

#Define playerDecision() function which prompts user for input. User input is stored in playerChoice #variable. If user inputs rock, paper, or scissors return playerChoice. If user enters anything other than #those three string choices perform a while loop to prompt user to enter rock, paper, or scissors. If player #inputs either of the three approved string values, exit while loop and return playerChoice variable.
def playerDecision():
    #Initialize playerChoice variable and prompt user for input
    playerChoice = input('Enter your choice of "paper", "rock", or "scissors": ')
    print('')
    
    #Determine if user inputted correct string values. If player enters anything other than the correct
    #string values, continue to prompt user to enter the correct string values. Return playerChoice variable
    if playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
        return playerChoice
    elif playerChoice != "rock" or playerChoice != "paper" or playerChoice!= "scissors":
        while playerChoice != "rock" or playerChoice != "paper" or playerChoice!= "scissors":
            print("YOU DID NOT ENTER ROCK, PAPER, OR SCISSORS HUMAN!\n")
            playerChoice = input('Please enter "paper", "rock", or "scissors" (or quit to exit): ')
            print('')
            if playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
                return playerChoice
            elif playerChoice == 'quit':
                exit()
        

#Define calculateChoices() function. This function determines whether the computer’s choice or the player’s #choice equals a win condition. If the player’s choice is equal to the computer’s choice the game calls the #restart() function.
def calculateChoices(aiPick,playerPick):
    if aiPick == "rock" and playerPick == "scissors":
        print('Computer Wins!!! Rock CRUSHES Scissors!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif aiPick == "scissors" and playerPick == "rock":
        print('Player Wins!!! Rock CRUSHES Scissors!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif aiPick == "scissors" and playerPick == "paper":
        print('Computer Wins!!! Scissors SHRED Paper!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif aiPick == "paper" and playerPick == "scissors":
        print('Player Wins!!! Scissors SHRED Paper!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif aiPick == "paper" and playerPick == "rock":
        print('Computer Wins!!! Paper ENGULFS Rock!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif aiPick == "rock" and playerPick == "paper":
        print('Player Wins!!! Paper ENGULFS Rock!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
    elif (aiPick == "rock" and playerPick == "rock") or \
    (aiPick == "scissors" and playerPick == "scissors") or \
    (aiPick == "paper" and playerPick == "paper"):
        print('Player and Computer TIED!\n')
        print('Computer picked: ', aiPick)
        print('Player picked: ', playerPick,'\n')
        restart(gameRestarts)

#Define restart() function. This function prompts the user to input a choice of y or n to continue playing #the game or to quit the program. A while loop is used to continue prompting the user for the correct string #values.
def restart(gameRestarts):
    start = 1

    while start == 1:
        choice = input("Would you like to start over? Y/N: ")
        print('')

        if choice == 'y' or choice == "Y":
            start = 2
            gameRestarts += 1            
            main(gameRestarts)
            return gameRestarts
            
        elif choice == 'n' or choice == 'N':
            start = 2
            exit()
        elif choice != ('y' or 'Y') or choice != ('n' or 'N'):
            print('YOU DID NOT ENTER Y/N!!!\n')
            restart(gameRestarts)

    
main(gameRestarts)
