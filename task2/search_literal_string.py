'''
Created on 11 Jun 2020

@author: blarico
'''
import random
import re

Sampletext = 'The quick brown fox jumps over the lazy dog.'
Searchedwords = ['fox', 'dog', 'horse']


def search_literal_strings(text, patterns):
    for pattern in patterns:
        print('Looking for "%s" in "%s" ->' %(pattern, text), end=' ')

        if re.search(pattern, text):
            print('Match found!')
        else:
            print('Match NOT found!')
