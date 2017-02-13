"""In this project, we'll build Rock-Paper-Scissors!

The program should do the following:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
Let's begin!"""

from random import randint
from time import sleep

#constant variables are declared in uppercase in snake case
OPTIONS = ["R", "P", "S"]
LOSS_MESSAGE = "You lost!"
WINNING_MESSAGE = "You won!"

def decide_winner(user_choice, computer_choice):
    print "You selected %s " % user_choice
    print "The computer selected %s " % computer_choice

    #.index() gets the item at the index from the OPTIONS list
    user_choice_index = OPTIONS.index(user_choice)
    computer_choice_index = OPTIONS.index(computer_choice)

    if user_choice == computer_choice:
        print "It's a tie!"
    elif user_choice_index == 0 and computer_choice_index == 2 or user_choice_index == 1 and computer_choice_index == 0 or user_choice_index == 2 and computer_choice_index == 1:
		print WINNING_MESSAGE
    elif user_choice_index > 2:
		print "You selected an invalid option."
    else:
		print LOSS_MESSAGE

def play_RPS():
    print "Rock, Paper, Scissors!"

    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
    user_choice = user_choice.upper()
    computer_choice = OPTIONS[randint(0, len(OPTIONS) - 1)]
    #call decide_winner function to access user_choice and computer_choice
    decide_winner(user_choice, computer_choice)

play_RPS()
