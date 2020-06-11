'''
Created on 11 Jun 2020

@author: blarico
'''
import random
import re

Sampletext = 'The quick brown fox jumps over the lazy dog.'
Searchedwords = ['fox', 'dog', 'horse']



def delete_duplicates(myList):
    #newList = list(dict.fromkeys(myList))  #Using 
    newList = []
    for element in myList:
        if element not in newList:
            newList.append(element)
    print(newList)
    return newList



