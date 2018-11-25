"""
This is a game where you have to guess the total amount of two dice, that have
been rolled simultaneously.
"""

from random import randint
from time import sleep


# Functions with 'get' in their name imply a 'return' at the end.
def get_user_guess():
    guess = int(raw_input("Enter guess: "))
    return guess


def roll_dice(number_of_sides):
    print "Welcome to Dice Number Guess!"
    print "Guess the total of a dice roll with two dice."

    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)

    max_val = number_of_sides * 2
    print "Highest possible guess is %d!\n" % max_val
    guess = get_user_guess()

    if guess > max_val:
        print "Guess must not be higher than %d!" % max_val

    else:
      print "Rolling..."
      sleep(2)
      print "First roll: %d" % first_roll
      sleep(1)
      print "Second roll: %d" % second_roll
      sleep(1)

      total_roll = first_roll + second_roll
      print "Total roll: %d" % total_roll
      print "Result..."
      sleep(1)

      if guess == total_roll:
        print "Good job! You've won!"
      else:
        print "You lost."

roll_dice(6)
