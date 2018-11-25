"""
This is a rock, paper, scissor game against the computer.
"""
from random import randint
from time import sleep
from termcolor import colored

global user_score
global computer_score

user_score = 0
computer_score = 0


options = ["ROCK", "PAPER", "SCISSORS"]

message = {
    "tie": "Yawn it's a tie!",
    "won": "Yay you won!",
    "lost": "Aww you lost!"
}


def decide_winner(user_choice, computer_choice):
    global user_score
    global computer_score
    print colored("Player Score: %d, Computer Score: %d", "green") % \
          (user_score, computer_score)
    print "Your choice is %s." % user_choice
    sleep(2)
    print "Computer's choice is %s.\n" % computer_choice

    if user_choice == computer_choice:
        print message["tie"]
        play_RPS()

    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
        print message["won"]

        user_score += 1
        play_RPS()

    elif user_choice == "PAPER" and computer_choice == "ROCK":
        print message["won"]
        user_score += 1
        play_RPS()

    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
        print message["won"]
        user_score += 1
        play_RPS()

    else:
        print message["lost"]
        computer_score += 1
        play_RPS()


def play_RPS():
    print "Welcome to Rock, Paper, Scissors!"
    user_choice = raw_input("Enter Rock, Paper, Scissors: \n")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)


play_RPS()