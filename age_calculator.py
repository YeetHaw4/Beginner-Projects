# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:48:15 2023

@author: spenc
"""

import datetime

today = datetime.datetime.now()

today_year = int(today.year)
today_month = int(today.month)
today_day = int(today.day)

birth_year = int(input("What year were you born? "))
birth_mx = input("What month? ").lower()
birth_day = int(input("What day? "))

if birth_mx == "january":
    birth_month = 1
elif birth_mx == "february":
    birth_month = 2
elif birth_mx == "march":
    birth_month = 3
elif birth_mx == "april":
    birth_month = 4
elif birth_mx == "may":
    birth_month = 5
elif birth_mx == "june":
    birth_month = 6
elif birth_mx == "july":
    birth_month = 7
elif birth_mx == "august":
    birth_month = 8
elif birth_mx == "september":
    birth_month = 9
elif birth_mx == "october":
    birth_month = 10
elif birth_mx == "november":
    birth_month = 11
elif birth_mx == "december":
    birth_month = 12
    
dif_year = today_year - birth_year
dif_month = today_month - birth_month
dif_day = today_day - birth_day

dif_year_days = dif_year * 365
if dif_year > 4:
    dif_year_days = (dif_year * 365) + (dif_year // 4)
dif_month_days = dif_month * (((7 * 31) + (4 * 30) + 28) / 12)
if dif_month < 0:
    dif_month = abs(dif_month * (((7 * 31) + (4 * 30) + 28) / 12))
if dif_day < 0:
    dif_day = abs(dif_day)

total_days = dif_year_days + dif_month_days + dif_day
total_years = int(total_days // 365)

print("You are " + str(total_years) + " years old.")
    
    