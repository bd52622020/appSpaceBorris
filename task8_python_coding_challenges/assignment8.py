'''
Created on 10 Jun 2020

@author: blarico
'''

import re


# Write a function that prints all the prime numbers between 0 and limit
# where limit is parameter

def prime_numbers(limit):
    for num in range(limit):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


prime_numbers(20)
    
# Given a year, report if it is a leap year

def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is NOT a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is NOT a leap year".format(year))

leap_year(2000)
    
# ISBN-10 verification process is used to validate book identification numbers
# these contains dashes e.g. 3-598-21508-8
# Validate the number is 10 digit ISBN

def isbn_verification(isbn):
    numbers = isbn.replace("-", "").replace(" ", "")
    match = re.search(r'(\d)-(\d{3})-(\d{5})-(\d)', isbn)
    if len(numbers) == 10 and match:
        print("isbn number: {0} is correct!".format(isbn))
    if len(numbers) != 10 and not match:
        print("isbn number: {0} is NOT correct!".format(isbn))
    if not match:
        print("isbn number: {0} is NOT correct!".format(isbn))
    
    
isbn_verification("3-h58-21508-8")    
    
# given a list of numbers, return true if first and last number is the same 

def numbers_compare(numbers):
    first_num = numbers[0]
    last_num = numbers[-1]
    if numbers[0] == numbers[-1]:
        print("{0} and {1} are equal!".format(numbers[0], numbers[-1]))
    if numbers[0] != numbers[-1]:
        print("{0} and {1} are NOT equal!".format(numbers[0], numbers[-1]))


numbers_compare([6, 1, 2, 3, 4, 5, 6])


    