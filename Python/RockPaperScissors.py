'''
Rock Paper Scissors
Dave Collins
'''
#Import
import random

#Variables
player = 0
opponent = 0
game = 0

#Main
def main():
    game = 1

    while game == 1:
        print("What do you want to throw?  1 for Paper, 2 for Scissors, 3 for Rock:")
        player = int(input())
        opponent = oppthrow()
        wincheck(player,opponent)

#Opponent Throw
def oppthrow():
    throw = random.randint(1,3)
    return throw

#Winner Check
def wincheck(player,opponent):
    if player == opponent:
        print("Tie game!")
        return
    elif player == 1:
        if opponent == 2:
            print("I win!!!!  You Loser!!!")
        else:
            print("You Win, I'm a big loser!!!!")
        return
    elif player == 2:
        if opponent == 3:
            print("I win!!!!  You Loser!!!")
        else:
            print("You Win, I'm a big loser!!!!")
        return
    elif player == 3:
        if opponent == 1:
            print("I win!!!!  You Loser!!!")
        else:
            print("You Win, I'm a big loser!!!!")
        return
    return

main()