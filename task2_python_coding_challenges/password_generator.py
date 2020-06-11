'''
Created on 11 Jun 2020

@author: blarico
'''
import random
import re

Sampletext = 'The quick brown fox jumps over the lazy dog.'
Searchedwords = ['fox', 'dog', 'horse']

def password_generator():
    try:
            passwordLength = int(input("Enter length of password: "))
    except ValueError:
        print("Invalid input")
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    password = ""
    for c in range(passwordLength):
        password += random.choice(chars)
    print(password)
    return(password)

    

