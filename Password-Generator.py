import random as rd

pwCharacters = 'ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyz0123456789!@#$_-'
pwCondition = False

def pwGenerator(pwQuantity, pwLength, pwCondition):
    print("There's a list of password you can used based on your choices:")

    if pwCondition == True:
        for x in range(pwQuantity):
            pwGenerated = ''
            for z in range(pwLength):
                pwGenerated += rd.choice(pwCharacters)
            print(pwGenerated)
    print("You choice", pwQuantity, "password(s) and", pwLength, "length of each password")
    return

print("This is a password generator... We'll help you to set a security password")
print("How many password you want to generate?")

pwQuantity = int(input("Quantity > "))

print("Now what the length of the password you want for each one?")
print("8 characters minimum and 32 characters maximum")

pwLength = int(input("Length > "))

while pwCondition == False:
    if (pwLength >= 8 and pwLength <= 32):
        pwCondition = True
        pwGenerator(pwQuantity, pwLength, pwCondition)
    
    else:
        if pwLength < 8:
            print("Password length is too short!")
            print("8 characters minimum and 32 characters maximum")
            pwLength = int(input("Length > "))
        elif pwLength > 32:
            print("Password length is too long!")
            print("8 characters minimum and 32 characters maximum")
            pwLength = int(input("Length > "))
