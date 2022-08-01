#! /bin/python
# Name: demo_lotto.py
# Author: Trish Saha
# Version: 1.0
# Description: This program will generate 6 random lottery numbers

"""
    Lottery Generator
"""

import pprint

# multi dimensional dict of lists
movies = { 'rafael': ['titanic', 'pride and prejudice', 'the notebook'],
           'michael': ['the school of rock', 'peanut butter falcon', 'incredibles'],
           'mayu': ['the lion king', 'sound of music', 'the fault in our stars']}

pprint.pprint(movies)

movies['donald']= ['the hobbit', 'the lord of the rings']

# ITERATE through the dict keys using an ITERATOR for loop
for name in movies.keys():
    print(f"{name}: {movies[name]}")

# ITERATE through the dict keys using an ITERATOR for loop
for (name, films) in movies.items():
    print(f"{name} likes {films}")

print(f"Michael's favourite movie is {movies['michael'][0]}")