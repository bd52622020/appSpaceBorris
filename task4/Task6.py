'''
Created on 1 Jun 2020

@author: blarico
'''

from datetime import datetime, timedelta
import re

def palindrome_Check(word):
    inverted = word[::-1]
    if word != inverted:
        print("Its not a palindrome!")
    if word == inverted:
        print("Its a palindome!")
    
    
def date_formats():
    today = datetime.datetime.today()
    print("Current date and time:", today.strftime("%b %d %Y %H:%M:%S"))
    print("Current year:", today.strftime("%Y"))
    print("Current month:", today.strftime("%b"))
    print("Week number of the year:", today.strftime("%W"))
    print("Weekday of the week:", today.strftime("%A"))
    print("Day of year:", today.strftime("%j")) 
    print("Day of the month:", today.strftime("%d"))
    print("Day of the week:", today.strftime("%d"))
    
def substracting_days():
    d = datetime.today() - timedelta(days=30)
    print(d)
    


def match(word):
    pattern = '^[a-zA-Z0-9_]'
    if re.search(pattern, word):
        print("Match found!")
    else:
        print("Match NOT found!")
    
    
