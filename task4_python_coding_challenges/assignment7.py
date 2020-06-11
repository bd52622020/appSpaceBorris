'''
Created on 9 Jun 2020

@author: blarico
'''
# Python function to check the speed of drivers
# Parameter speed 
from random import randrange
import sys

def speed_check(speed):
    demerit_points = 0
    if speed < 70:
        print("OK")
    
    speed = speed - 70
    while speed > 0 :
        demerit_points+=1
        speed = speed - 5
        
        
    if demerit_points !=0:
        print("Points:", demerit_points)
        
    if demerit_points > 12:
        print("License suspended!")
        
        
speed_check(200)

def read_file(file_name):
    try:
        with open(file_name, "r") as f:
            num_lines=10
            file_content = [next(f) for _ in range(num_lines)]
            for line in file_content:
                print(line)
        if not file_content:
            print("No data in file: ", file_name)
    
    except IOError as e:
        print("I/O error ({}): {1}".format(e.errno, e.strerror))
    except:
        print("Unexpected error;", sys.exc_info()[0])
    finally:
        print("File might not have 10 lines to print")
            
        
read_file("regextask.txt")


def triangle_range(side1, side2):
    max_range = side1 + side2
    min_range = abs(side1 - side2)
    print("The range of the triangle is between: {0} < x < {1}".format(min_range, max_range))
    
triangle_range(9, 2)
    
    
def score_calculator(name="", wins=0, losses=0, draws=0):
    random_number= randrange(3)
    total_points=0
    good_taunts={1: "YOU ARE ON FIRE!", 2:"kinda average!", 3: "NICEEE!"}
    bad_taunts={1: "Not to bad", 2: "EEERRggg", 3: "LOSSSERS!"}
    for _ in range(wins):
        total_points+=3
    for _ in range(losses):
        total_points+=1

    if total_points < 20:
        print("the team {0} has a total points of: {1}".format(name, total_points))
        print(good_taunts[random_number])
        
    if total_points > 20:
        print("the team {0} has a total points of: {1}".format(name, total_points))
        print(bad_taunts[random_number])
        
    
score_calculator("Jacks", 20, 2, 1)

        