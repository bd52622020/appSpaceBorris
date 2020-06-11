'''
Created on 11 Jun 2020

@author: blarico
'''
import random
import re

Sampletext = 'The quick brown fox jumps over the lazy dog.'
Searchedwords = ['fox', 'dog', 'horse']


    
def rock_paper_scissors():
    keep_playing = "Yes"
    while keep_playing == "Yes":
        player1 = input("Player 1: Rock, Paper, Scissor? ")
        player2 = input("Player 2: Rock, Paper, Scissor? ")

        if player1 == player2:
            print("Its a tie!")
        if player1 == "Rock" and player2 == "Scissor":
            print("Congratulations player1!")
        if player1 == "Paper" and player2 == "Rock":
            print("Congratulations player1!")
        if player1 == "Scissor" and player2 == "Paper":
            print("Congratulations player1!")
        if player2 == "Rock" and player1 == "Scissor":
            print("Congratulations player1!")
        if player2 == "Paper" and player1 == "Rock":
            print("Congratulations player1!")
        if player2 == "Scissor" and player1 == "Paper":
            print("Congratulations player1!")
        
        keep_playing = input("Start a new game Yes or No?")        


