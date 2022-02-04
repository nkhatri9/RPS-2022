


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#

import random
import os

#allow the user to configure their own player name by passing an environment variable called PLAYER_NAME
player_name = os.getenv("PLAYER_NAME", default="Player One")

def determine_winner(userMove, computerMove):
    #user chooses rock
    gameResult = None
    if userMove == "rock" and computerMove == "paper":
        print("You lose!")
    elif userMove == "rock" and computerMove == "scissors":
        print("You win!")
    elif userMove == "rock" and computerMove == "rock":
        print("It's a tie!")

    #user chooses paper

    if userMove == "paper" and computerMove == "scissors":
        print("You lose!")
    elif userMove == "paper" and computerMove == "rock":
        print("You win!")
    elif userMove == "paper" and computerMove == "paper":
        print("It's a tie!")

    #user chooses scissors
    if userMove == "scissors" and computerMove == "rock":
        print("You lose!")
    elif userMove == "scissors" and computerMove == "paper":
        print("You win!")
    elif userMove == "scissors" and computerMove == "scissors":
        print("It's a tie!")
    
def main():

    print("Hi", player_name + "!")

    #list of possible user moves
    choiceList = ["rock", "paper", "scissors"]

    #Welcome User to game
    print("Welcome to my rock, paper, and scissors game!")

    #Get user input convert to lower case
    userChoice = None

    #make sure user chooses valid input
    while userChoice not in choiceList:
        userChoice = input("Please type in rock, paper, or scissors: ").lower()
        print()
    
    #Tell user what they chose
    print("You chose", userChoice + "!")

    #computer selects move
    computerChoice = random.choice(choiceList)

    print("The computer chose", computerChoice)

    #determine who wins
    determine_winner(userChoice, computerChoice)

main()