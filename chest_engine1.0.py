"""
This script is supposed to be the back-end of a loot chest used in video-games.
"""

from termcolor import colored

# Chest Switch:
chest_a = 1


# Menu:
def start():
	print "Play game?"
	print colored("\t Yes", "green"), "|", colored("No", "red")
	answer = raw_input("> ")
	if answer == "yes":
		print colored("game is starting...", "green")
		map()
	else:
		print "Too bad, you don't have a choice!"
		start()


# Enter Map:
def map():
	#chest = 1
	print "I have arrived in a dungeon."
	print "I see a a red chest in front of me."
	print "should I open the chest?"
	print colored("\t Yes", "green"), "|", colored("No", "red")

	answer = raw_input("> ")

	if answer == "yes":
		chest()
	else:
		map()


# Chest Engine:
def chest():
	global chest_a
	if chest_a == 1:
		print "You found", colored("500 gold", "yellow"), "!\n"
		chest_a += 1
		map()
	else:
		print "Chest is empty..."

# Start Game:
start()
