# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:19:19 2023

@author: spenc
"""

import random

print("Welcome to the Angle Game")
play_or_not = input("Would you like to play? y/n ")

x = 0

def angle_game():
    
    for i in range(0, 10):
    
        global x
        
        angle = random.randint(0, 359)
    
        if angle >= 0 and angle <= 30:
            name = "acute"
        elif angle > 30 and angle <= 90:
            name = "normal"
        elif angle == 90:
            name = "right"
        elif angle > 90 and angle <= 180:
            name = "obtuse"
        elif angle > 180 and angle <= 359:
               name = "reflex"
    
        guess = input("What type of angle is " + str(angle) + " degrees? ").lower()
    
        if guess == name:
            x += 1
            
    print("You got " + str(x) + " out of ten")
    return(x)

if play_or_not == "y":
    angle_game()
    
else:
    print("okay")