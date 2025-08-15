'''
Basic Password Game
Dave Collins
'''

def valid(word):

    if len(word) <5 or len(word) > 20: #checks password length, returns false if too short/long.
        print("Your password is too tiny or maybe too big...")
        return False 
    
    if not uppercase(word): #Checks password for an uppercase letter, returns false if none.
        print("Your password is weak, with no capital letters...")
        return False
    
    if not lowercase(word): #Checks password for a lowercase letter, returns false if none
        print("Your password is way to big with no small letters")
        return False
    
    if not number(word): #checks password for a number, if none returns false.
        print("Your password isn't enough of a nerd, give it some numbers")
        return False
    
    if not special(word): #Checks password for a special character, if none return flase
        print("Your password needs to feel more special, give it some special characters")
        return False
    
    return True

def uppercase(string): #checks for an uppercase letter
    for element in string:
        if ord(element) >= 65 and ord(element) <=90: #uppercase check
            return True
    return False

def lowercase(string): #checks for a lowercase letter
    for element in string:
        if ord(element) >=97 and ord(element) <=122: #Lowercase Check
            return True
    return False

def number(string):
    numbers = "1234567890" #create the reference
    for element in string: #Check the individual chracters
        for char in numbers: #check against the numbers list
            if element == char: #if there is a match...
                return True #send back yuppers
    return False

def special(string):
    specials = "!@#$%^&*" #reference list of special characters
    for element in string: #check the individual characters
        for char in specials: #check the reference
            if element == char: # if matched...
                return True #Say aye.
    return False

def main():
    print("Greetings mortal, I am here to help you pick a good password!")
    password = input("Give me a password you want to use:")
    while not valid(password):
        print("Like you, your password is WEAK!  Try again")
        password= input("Give me a better password:")
    
    print("Congrats! Your password is strong and mighty!")


main()