# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:02:24 2023

@author: spenc
"""

import random
import sys

x = []
y = []
z = []
a = []

file = open("C:/Users/spenc/OneDrive/Desktop/Python Scripts/Input_Files/words.txt","r")

for line in file:
    x.append((line.strip()))

word = random.choice(x).lower()

for i in word:
    y.append(i)
    z.append("_ ")
    
chances = 12

while "_ " in z:
    guess = input("Guess a letter ").lower()
    if guess in a:
        guess = input("Choose a new letter ").lower()
    a.append(guess)
    for i in range(len(y)):
        if y[i] == guess:
            z[i] = guess
    print("".join(z))
    print("Letters guessed: " + "".join(a))
    
    chances -= 1
    print("Chances left = " + str(chances))
    
    if chances == 0:
        print("")
        print("You lose")
        print("The word was " + "".join(y))
        sys.exit()
        
else:
    print("")
    print("You win! Congratulations")
    sys.exit()