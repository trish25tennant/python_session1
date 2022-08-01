#! /bin/python
# Name: demo_lotto.py
# Author: Trish Saha
# Version: 1.0
# Description: This program will generate 6 random lottery numbers

"""
    Lottery Generator
"""
import random

lotto= []


while len(lotto)<6:
    num = random.randint(1, 50)
    lotto.append(num)

print(f"Lottery numbers {lotto}") # Example of f-strings
lotto=[]
# while len(lotto) < 6:
#    num = random.randint(1, 50)
#   if num not in lotto:
#        lotto.append(num)
#    else:
#        print(f"Duplicate number {num}")
# can format strings

lotto = {}
print(type(lotto)) # automatically class dict

lotto = set() #  create an empty set

# will only add unique numbers
while len(lotto) < 6:
    num = random.randint((1, 50))
    lotto.add(num)

