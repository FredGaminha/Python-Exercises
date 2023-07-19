import random as rd

def userTries(tries):
    print(f'You missed! Now you have {tries} tries left')

    if tries == 7:
        print("You already missed three times... You want a tip?")
        print("[1] - Yes | [2] - No")
        userTip = int(input("Your choice > "))

        if userTip == 1:
            OddOrEven = pcRandomizer % 2

            if OddOrEven == 0:
                print("The number is EVEN")
                mainGame(tries)
            else:
                print("The number is ODD")
                mainGame(tries)
        elif userTip == 2:
            print("You decided to not use any tip... Good luck!")
            mainGame(tries)
    elif tries == 3:
        print("You already missed seven times... You want another tip?")
        print("[1] - Yes | [2] - No")
        userTip = int(input("Your choice > "))

        if userTip == 1:
            print("My number is between ", pcRandomizer - lowRandomizer, " and ", pcRandomizer + highRandomizer)
            mainGame(tries)
        elif userTip == 2:
            print("You decided to not use any tip... Good luck!")
            mainGame(tries)
    else:
        mainGame(tries)
    return
        
def mainGame(tries):
    if tries != 0:
        userGuess = int(input("Type another number > "))
        if userGuess == pcRandomizer:
            print("You guessed my number!")
        else:
            tries = tries - 1
            userTries(tries)
    elif tries == 0:
        print("Game Over! I was thinking on number ", pcRandomizer)
    return

pcRandomizer = rd.randint(1,100)
lowRandomizer = rd.randint(1,10)
highRandomizer = rd.randint(1,10)
tries = 10

print("Guessing Game!")
print("I think in a number between 1 and 100... Now, try to guess what number i was thinking")
print("I'll give you 10 tries and i'll offer a tip after missing five times")

userGuess = int(input("Type a number > "))

if pcRandomizer == userGuess:
    print("You guessed on your first try! Nice work!")
else:
    tries = tries - 1
    userTries(tries)


