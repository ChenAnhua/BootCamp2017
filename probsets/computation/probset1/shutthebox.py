# -*- coding: utf-8 -*-
"""
Script for shut the box game
"""

import random
import box as box
import sys

# We firstly print the name of the player
if len(sys.argv) != 2:
    player_name = input("Please enter your name: ")
else:
    player_name = ''.join(sys.argv[1:])

# set some initial parameters
remaining_list = list(range(1,10))
stopper = True

while stopper:
    print("\nNumbers left: ", remaining_list) # prinitng the remaining list
    # generate the dice roll
    if (sum(remaining_list) > 6):
        roll = random.choice(list(range(2, 13))) # generate a random 2-dice roll
    else:
        roll = random.choice(list(range(1, 7))) # generate a random 1-dice roll
    print("Roll: ", roll)
    stopper = box.isvalid(roll, remaining_list)
    if stopper:
        player_input = input("Numbers to eliminate: ")
        elimination = box.parse_input(player_input, remaining_list) 
        while not elimination or sum(elimination) != roll:
            print("Invalid output!")
            player_input = input("Numbers to eliminate: ")
            elimination = box.parse_input(player_input, remaining_list)
        remaining_list = [n for n in remaining_list if n not in elimination]
    #stopper =  box.isvalid(roll, remaining_list)
    else:
        print("Game over!")
#print("Game over!")
score = sum(remaining_list)
print("\n Score for ", player_name, ": ", score)
if score == 0:
    print("Congrats! You shut the box!")


