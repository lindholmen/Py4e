#! /usr/bin/env python3

#from random import randint, choice
import random
player1 = input("Enter your choice!\n")

while player1 == "paper" or player1 == "scissor" or player1 == "rock":
    player2 = random.choice(["paper", "rock", "scissor"])
    print("player2 is ", player2)
    if (player1 == player2):
        print("It is a draw")
    elif player1 == "paper" and player2 == "rock":
        print("You win!")
    elif player1 == "rock" and player2 == "scissor":
        print("You win!")
    elif player1 == "scissor" and player2 == "paper":
        print("You win!")
    else:
        print("You lose!")
    player1 = input("Enter your choice!\n")
