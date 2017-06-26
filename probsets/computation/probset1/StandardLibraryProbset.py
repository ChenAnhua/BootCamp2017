# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 21:05:46 2017

@author: CHEN Anhua
"""
#import numpy as np
import calculator as cal
import box
import random


# prob1
prob1 = lambda my_list: [min(my_list), max(my_list), sum(my_list)/len(my_list)]

# prob2
#numbers

numbers  = 3
numbers2 = numbers
numbers2 += 1
if numbers == numbers2:
    print("numbers:", " mutable")
else:
    print("numbers:", " immutable")

#strings
strings  = "uchicago"
strings2 = strings
strings2 += 'a'
if strings == strings2:
    print("strings:", " mutable")
else:
    print("strings:", " immutable")

#lists
lists  = [1,2,3]
lists2 = lists
lists2.append(1)
if lists == lists2:
    print("lists:", " mutable")
else:
    print("lists:", " immutable")


#tuples
tuples = (1, 2, 4)
tuples2 = tuples
tuples2  += (1,)
if tuples == tuples2:
    print("tuples:", " mutable")
else:
    print("tuples:", " immutable")

# dictionaries
dictionary = {1: "b", 2: "x"}
dictionary2 = dictionary
dictionary2[1] = 'a'
if dictionary == dictionary:
    print("dictionary:", " mutable")
else:
    print("dictionary:", " immutable")


# prob3
# the calculator.py is stored in the same directory
def newfunc(a, b):
    result = cal.sqrtcal(cal.sumcal(cal.productcal(a,a), cal.productcal(b,b)))
    return result
print(newfunc(3, 4))


#prob4

# shut the box game
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
