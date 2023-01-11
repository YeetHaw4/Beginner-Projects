# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:13:04 2023

@author: spenc
"""

import random

print("Welcome to penalty kicks")

options = {"tl":1, "bl":1, "tm":3, "bm":4, "tr":5, "br":6}

shot = input("Where would you like to aim? TL, BL, TM, BM, TR, BR? ").lower()

ball = options[shot]
    
block = random.randint(1,6)

if block == 1:
    block2 = 2 or 3
elif block == 2:
    block2 = 1 or 4
elif block == 3:
    block2 = 1 or 4 or 5
elif block == 4:
    block2 = 2 or 3 or 6
elif block == 5:
    block2 = 3 or 6
elif block == 6:
    block2 = 4 or 5


if block == ball or block2 == ball:
    print("Shot blocked")
else:
    print("Goal")
    