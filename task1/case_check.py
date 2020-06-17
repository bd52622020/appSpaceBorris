'''
Created on 2 Jun 2020

@author: blarico
'''
def case_letter_counter(words):
    upper=0
    lower=0
    for letter in words:
        if letter.isupper():
            upper+=1
        if letter.islower():
            lower+=1
    print("Upper case:", upper)
    print("Lower case:", lower)
    



    
