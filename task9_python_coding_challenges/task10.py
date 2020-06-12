from itertools import groupby
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Remove the consecutive duplicates of a list
def remove_duplicates(myList):
    items= [x[0] for x in groupby(myList)]
    print(items)
    return items

my_list= [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
remove_duplicates(my_list)

# Write a Python program to create a lambda function that adds 15
# to a given number passed in as an argument

def add_15(num):
    result = lambda num: num + 15
    print(result(num))

add_15(15)

# create a lambda function that multiplies argument a with argument b 
# and print the result

def multiply(num1, num2):
    result = lambda num1, num2 : num1 * num2
    print(result(num1, num2))

multiply(2,5)

# Write a Python program to find numbers divisible by nineteen or thirteen 
# from a list of numbers using Lambda

def divisible_by_19_13(numList):
    result = list(filter(lambda num: (num % 19 == 0 or num % 13 == 0), numList))
    print(result)

divisible_by_19_13([13, 19, 24, 35])

# Write a Python program to extract and display all the header tags from
# en.wikipedia.org/wiki/Main_Page

def extract_headers(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    headers = bs.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    print(headers)


url = "en.wikipedia.org/wiki/Main_Page"
extract_headers(url)