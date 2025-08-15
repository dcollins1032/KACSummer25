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
    print("2. 5 color choices")
    print("3. 6 color choices (in future version)")

    game = int(input("Choose:"))
    password = ['X','X','X','X']

    if game == 1:
        password = easymode(password)
    elif game == 2:
        password = mediummode(password)

    gameloop(password)
 
def gameloop(password):
    victory = 0 #victory checker
    while victory == 0: #start main game loop
        guess = input("Give me your guess:") #take in the guess
        lettercheck(guess, password) #send the password and guess to the checker
        victory = positioncheck(guess, password)



def lettercheck(guess, password):
    matchletters = 0 #variable to track how many letters are matched
    breaker = 0 #escape variable for loops because reasons
    for i in range(4): #for loop for iterating the guess
        for j in range(4): # for loop for iterating the password
            if breaker == 1: #checks if the escape variable is set
                continue
            if guess[j] == password[i]: #iterates through comparing the letters
                matchletters += 1 #boop up the tracker
                breaker = 1 #escape variable set
                continue
        breaker = 0 #resets the escape variable
    print("you have", matchletters, "colors correct") #let the player know how many colors they have picked correctly
    return

def positioncheck(guess, password): #checking if the guesses line up to the password
    correct = 0 #victory tracker
    for i in range(4): #check each digit of the password and guess
        if guess[i] == password[i]: #check if the current digits match
            correct+= 1 #yay
    if correct == 4: #check for victory
        print("You Win!")
        return True # Yeet back a victory
    else: #no victory
        print("You have", correct, "colors in the right places")
        return False #fail




def easymode(password2):
    password = [0,0,0,0]
    for element in range(4):
        password[element] = random.randint(1,4)
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

    print("I've got a password, lets get ready to play!!!")
    print("This game will have a password that only contains Red Blue yellow or Green, represeted by R G Y or B")
    print("Your guesses should be a group of 4 letters like: RGBY")
    print("The same color can be used more than once.")
    print("You will receive some hints...")
    
    return password2


def mediummode(password2):
    password = [0,0,0,0]
    for element in range(4):
        password[element] = random.randint(1,5)
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
        elif password[element] == 4:
            password2[element] = 'Y'
            continue
        else:
            password2[element] = 'O'

    print("I've got a password, lets get ready to play!!!")
    print("This game will have a password that only contains Red Blue yellow Orange or Green, represeted by R G Y O or B")
    print("Your guesses should be a group of 4 letters like: RGBY")
    print("The same color can be used more than once.")
    print("You will receive some hints...")
    
    return password2



main()