# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:08:48 2023

@author: spenc
"""

import random

question1 = input("Would you like to generate a random password? Y/N ")

if question1 == "Y":
    how_long = int(input("How many characters would you like your password to be? "))
    
x = []

characters = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$_")

for i in range(0, how_long):
    random_character = random.choice(characters)
    x.append(random_character)

print("".join(x))