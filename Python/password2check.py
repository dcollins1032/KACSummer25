'''
Password Cracker Game
Dave Collins
'''
import random

#4 colors:  Red, Green, Yellow, Blue


def main():
    print("Welcome to Password Cracker!!!!")
    print("In this games you will try to crack")
    print("A password using 4 colors.")
    print("I will give you a hint, if you pick a correct color")
    print("If you get it in the right spot, I will let you know!")
    print("Select Difficulty:")
    print("1. 4 color choices")
    print("2. 5 color choices (in future version)")
    print("3. 6 color choices (in future version)")

    game = int(input("Choose:"))
    password = ['X','X','X','X']

    if game == 1:
        password = easymode(password)

    gameloop(password)
    
def gameloop(password):
    victory = 0  
    while victory == 0:
        guess = input("Give me your guess:")
        lettercheck(guess, password)
        positioncheck(guess, password)
        print(password)
        #victory = positioncheck(guess, password)


def lettercheck(guess, password):
    matchletters = 0
    breaker = 0
    for i in range(4):
        for j in range(4):
            if breaker == 1:
                continue
            if guess[j]== password[i]:
                matchletters += 1
                print("Check:",guess[i],"vs",password[j], "check:", i, " ", j, "Good Match")
                breaker = 1
                continue
            else:
                print("Check:",guess[i],"vs",password[j], "check:", i, " ", j, "Bad Match")
        breaker = 0    
        
        print("oof")

                
    print("You have",matchletters,"colors correct")
    return

def positioncheck(guess, password):
    correct = 0
    for i in range(len(password)):
        if guess[i] == password[i]:
            correct += 1
    if correct == 4:
        print("You win!")
        return True
    else: 
        print("You have",correct,"Colors in the right place")
        return False








def easymode(password2):
    password = [0,0,0,0]
    for element in range(4):
        password[element] = random.randint(1,4)
        print(password[element])
    for element in range(4):
        if password[element] == 1:
            password2[element] = 'R'
            continue
        elif password[element] == 2:
            password2[element] = 'G'
            continue
        elif password[element] == 3:
            password2[element] = 'Y'
            continue
        else:
            password2[element] = 'B'
    print("I've got a password, lets get ready to play!")
    print("This game will have a password that only contains Red Blue Yellow or Green, represented by R G Y or B")
    print("Your guesses should be a group of 4 letters like:  RGBY")
    print("The same color can be used more than once.")
    print("You will receive some hints...")

    return password2




main()