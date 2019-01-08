# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:41:13 2019

@author: Ruddy
"""


import json
#from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("dictionary.json"))

#value = SequenceMatcher(None, "mokeyy", "monkey").ratio()
#print(value)

def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return("The word doesn't exist.")
        else:
            return("The word doesn't exist 2")

#input from the user
word_user = input("Enter a word :")
#retrive word
output = retrive_definition(word_user)

if type(output)==list:
    for item in output:
        print("-", item)
else:
    print("-", output)

#print(retrive_definition(word_user))