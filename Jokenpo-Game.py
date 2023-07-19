import random as rd
import time as tm

pcOptions = ["Rock", "Paper", "Scissors"]
userOptions = ["Rock", "Paper", "Scissors"]
GameOver = False

print("A very simple Rock, Paper, Scissors Game!")
print("The rules are simple, you just need to choose a option that beat my option")
print("One of the following scenarios can happen")
print("1. Rock beats Scissors")
print("2. Paper beats Rock")
print("3. Scissors beats Paper")


while GameOver == False:
    pcChoice = rd.choice(pcOptions)
    print("I already made my choice, now it's your turn")
    print("Choose a option from below:")
    print("[1] - Rock")
    print("[2] - Paper")
    print("[3] - Scissors")

    userChoice = int(input("Your option > "))

    if userChoice == 1 or userChoice == 2 or userChoice == 3:
        #Rock Scenarios
        if userChoice == 1 and pcChoice == "Rock":
            print("It's a draw... Let's try again!")
            tm.sleep(2)
        elif userChoice == 1 and pcChoice == "Paper":
            print("I won with Paper!! You lose! Better luck next time")
            GameOver = True
        elif userChoice == 1 and pcChoice == "Scissors":
            print("You won! Good job! It was fun!")
            GameOver = True
        
        #Paper Scenarios
        if userChoice == 2 and pcChoice == "Rock":
            print("You won! Good job! It was fun!")
            GameOver = True
        elif userChoice == 2 and pcChoice == "Paper":
            print("It's a draw... Let's try again!")
            tm.sleep(2)
        elif userChoice == 2 and pcChoice == "Scissors":
            print("I won with Scissors!! You lose! Better luck next time")
            GameOver = True

        #Scissors Scenarios
        if userChoice == 3 and pcChoice == "Rock":
            print("I won with Rock!! You lose! Better luck next time")
            GameOver = True
        elif userChoice == 3 and pcChoice == "Paper":
            print("You won! Good job! It was fun!")
            GameOver = True
        elif userChoice == 3 and pcChoice == "Rock":
            print("It's a draw... Let's try again!")
            tm.sleep(2)
    
    else:
        print("Invalid option... Type again")
        tm.sleep(2)