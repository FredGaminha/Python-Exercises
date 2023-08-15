import random as rd
import time
import os

def newCards():
    card = rd.choice(cards)
    cards.remove(card)
    userHand.append(card)

    print(f'You receive the card {card}')

    sumCards(userHand)
    return

def sumCards(userHand):
    sumCard = 0

    for i in userHand:
        sumCard += i

    if sumCard == 21:
        print("You made a blackjack! Well done!")
        time.sleep(1)
        os.system('CLS')
        GameOver = False
        return GameOver

    elif sumCard > 21:
        print(f'You busted with {int(sumCard)}! You lose!')
        time.sleep(1)
        os.system('CLS')
        return GameOver
    
    elif sumCard < 21:
        print(f'Now your score is {int(sumCard)}, wanna continue? [Y] - YES | [N] - NO')
        coninueOption = input("Option > ").lower
        
        if coninueOption == 'y':
            continueGame()
            os.system('CLS')
        elif coninueOption == 'n':
            print("You give up with" + sumCard)
    return

def continueGame():
    if GameOver == True:
        print("Select a action - [H] Hit | [Q] Quit")
        userOption = input("> ").lower()

        if userOption == "h":
            newCards()

    elif GameOver == False:
        return GameOver

cards = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
userHand = []
dealerHand = []
GameOver = True

print("Let's play a quick game of Blackjack")
print("The rules are simple:")
print("1- You need to stack cards to add 21 in your hand")
print("2- The card's value is 1 to 11 and there's no doubles!")
print("3- Go over 21 and you lose!")

print("\n")
time.sleep(2)

while GameOver == True:
    continueGame()
