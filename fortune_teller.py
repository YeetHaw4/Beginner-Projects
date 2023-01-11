# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:09:03 2023

@author: spenc
"""

print("This is the fortune teller game")
color1 = input("Do you want red, green, blue, or yellow? ")

color = color1.lower()

if color == "red":
    x = 90
    possible_1 = 1
    possible_2 = 8
elif color == "green":
    x = 100
    possible_1 = 3
    possible_2 = 7
elif color == "blue":
    x = 110
    possible_1 = 2
    possible_2 = 6
elif color == "yellow":
    x = 120
    possible_1 = 4
    possible_2 = 5
    
number = int(input("Pick " + str(possible_1) + " or " + str(possible_2) + " "))

if x + number == 91:
    print("You will be president")
elif x + number == 98:
    print("You will be king")
elif x + number == 103:
    print("You will be a millionaire")
elif x + number == 107:
    print("You will be a billionaire")
elif x + number == 112:
    print("You will be an athlete")
elif x + number == 116:
    print("You will be a singer")
elif x + number == 124:
    print("You will have a big family")
elif x + number == 125:
    print("You will have an easy life")
else:
    print("Please pick a valid number next time")
    






