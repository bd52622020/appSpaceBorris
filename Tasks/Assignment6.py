'''
Created on 8 Jun 2020

@author: blarico
'''
# 1) Create a function that takes a dictionary of student names and returns a list of student
# names in alphabetical order



def print_names(namesdict):
    list_names=[]
    list_of_elements= namesdict["firstname"]
    for name in list_of_elements:
        list_names.append(name)
    
    print(list_names)
    
   
namesdict = {'firstname': ['Boris','Jhon',"Marco"], 'lastname': ['johnson', 'Manuel', 'tim']}

print_names(namesdict)


# 2) Write a python class which has two methods 
# get_string: accept a string from the user
# print_string: print the string in upper case

class Myclass:
    def __init__(self, myString):
        self.mystring= myString
    
    def get_string(cls):
        return cls(
            raw_input("myString: ")
            )
        
    def print_string(self):
        print(self.get_string())


#test = Myclass.get_string()

# 3) write a python program to check the validity of password input by users
# - At least 1 letter [a-z] and 1 letter [A-Z]
# - At least 1 number [0-9]
# - at least 1 char [$#@]
# - Min length 6
# - Max length 16


def password_check(password):
    lowercase= 0
    uppercase= 0
    number= 0
    char= 0
    minlength= 0
    maxlength= 0
    
    if len(password) > 6 and len(password) < 17:
        minlength+=1
        maxlength+=1
    
    for char in password:
        if char.islower():
            lowercase+=1
        if char.isupper():
            uppercase+=1
        if char.isdigit():
            number+=1
        print(char)
    
    if lowercase and uppercase and number and char and minlength and maxlength == 1:
        print("Password secure!")
        
    print("Password not secure!")

#password_check("dkjashfj3f3f")

# 4) contruct patter using nested for loop
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *
#  * * * *
#  * * *
#  * * 
#  *

def pattern_printer():
    num=6
    for i in range(num):
        for x in range(i):
            print("*", end=" ")
        print()
    for i in range(num,0,-1):
        for x in range(i):
            print("*", end=" ")
        print()
 
pattern_printer()


