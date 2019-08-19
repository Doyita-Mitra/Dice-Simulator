#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on Aug 18, 2019
# @author: Doyita Mitra

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on Aug 18, 2019
# @author: Doyita Mitra

import json
from difflib import get_close_matches

data = json.load(open("/Users/doyitamitra/Downloads/data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        user_input = input("Did you mean {} instead? Enter Y or N: ".format(get_close_matches(word, data.keys())[0]))

        if user_input == "Y".lower():
            return data[get_close_matches(word, data.keys())[0]]

        elif user_input == "N".lower():
            return "The word doesn't exist. Please double check it."

        else:
            return "Did not understand the word you typed. Bye!"
        
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

result = translate(word)

if isinstance(result, list):
    for w in result:
        print(w)
else:
    print(result)
