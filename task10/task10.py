'''
Created on 15 Jun 2020

@author: blarico
'''
import random
import string

def vehicles_bellow_5000(my_dict):
    vehicels = []
    for key in my_dict:
        if my_dict.get(key) < 5000:
            vehicels.append(key)
    print(vehicels)


my_dict={"Sedan": 1500,"SUV": 2000,"PickUp": 2500,"Minivan": 1600,"Van": 2400,"Semi": 13600,"Motorcycle": 110}
vehicles_bellow_5000(my_dict)

def square_list(my_list):
    new_list = []
    for num in my_list:
        new_list.append(num * num)
    print(new_list)


my_list=[10, 20, 30, 40, 50 ,60]
square_list(my_list)


def birthday_check(my_dict):
    name = input("Enter name: ")
    if name in my_dict:
        print(my_dict.get(name))
    if name not in my_dict:
        print("name not found")

   
my_birthday={"Boris": "01/10/1995","Suban": "01/02/1995","Carl": "21/10/1995","Jonathat": "21/04/1995","Van": "01/10/1995","Semi": "01/10/1995","Pan": "01/10/1995"}
birthday_check(my_birthday)


def password_generator(password_length=15):
    password_chars=string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(password_length):
        password = password + random.choice(password_chars)
    print(password)
    


password_generator(20)


