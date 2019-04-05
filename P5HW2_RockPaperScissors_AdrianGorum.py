# A brief description of the project
# 4-4-2019
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Adrian Gorum
#

import random

MIN = 1
MAX = 3
gameRestarts = 0

def main(gameRestarts):
    
    if gameRestarts == 0:
        print("LET'S PLAY ROCK, PAPER, SCISSORS HUMAN!!!\n")
    elif gameRestarts > 0:
        print("LET'S PLAY AGAIN!!!\n")
        
    aiRandom = random.randint(MIN,MAX)
    aiPick = aiDecision(aiRandom)
    playerPick = playerDecision()
    calculateChoices(aiPick,playerPick)
    restart(gameRestarts)    


def aiDecision(aiRandom):
    aiChoice = "str"

    if aiRandom == 1:
        aiChoice = "rock"
    elif aiRandom == 2:
        aiChoice = "paper"
    elif aiRandom == 3:
        aiChoice = "scissors"

    return aiChoice

def playerDecision():
    playerChoice = input('Enter your choice of "paper", "rock", or "scissors": ')
    print('')
    
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
