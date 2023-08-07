#!/usr/bin/env python3

import ipdb

def return_evens(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
    if even_numbers:
            return even_numbers
    else:
            return[]
    


    

def make_exclamation(sentence_list):
    add_exclamation = []
    for sentence in sentence_list:
         exc_point = sentence + "!"
         add_exclamation.append(exc_point)
    return add_exclamation
#ipdb.set_trace()