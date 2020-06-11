'''
Created on 11 Jun 2020

@author: blarico
'''

import os
from IPython.core.magic_arguments import argument
from _dbus_bindings import Dictionary

def os_info():
    home = os.environ['HOME']
    
    print("The user's home is: {0}".format(home))
    print("Operating system dependent module: {0}".format(os.name))
    
os_info()

def right_angle_triangle(len1, len2, len3):
    angles = [len1, len2, len3]
    hypotenuse= max(angles)
    x = hypotenuse * hypotenuse
    y = len1 * len1 + len2 * len2
    if x == y:
        print("Its a right angle triangle!")
    if x != y:
        print("Its NOT a right angle triangle")
        
right_angle_triangle(12, 35, 37)


def dic_concatenation(dictionaries):
    total = {}
    for dictionary in dictionaries:
        total.update(dictionary)
    print(total)
    
dictionaries = [{1:2, 3:4}, {5:6, 7:8}, {9:10, 11:12}]

dic_concatenation(dictionaries)


def check_key_in_dict(key, dict):
    if key in dict:
        print("Key exists!")
    if key not in dict:
        print("Key does NOT exist!")
    

check_key_in_dict(4, {1:2, 2:3, 3:4})
    

