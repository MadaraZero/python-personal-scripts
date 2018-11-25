# - IMPORTS -
import webbrowser
from sys import exit
from termcolor import

# - GRAPHICS -
title = ("""
---------------------------oOOo-------------------------

   ____                  _     _______ _
  / __ \                | |   |__   __(_)
 | |  | |_   _  ___  ___| |_     | |   _ _ __ ___   ___
 | |  | | | | |/ _ \/ __| __|    | |  | | '_ ` _ \ / _ \\
 | |__| | |_| |  __/\__ \ |_     | |  | | | | | | |  __/
  \____\_\__,_|\___||___/\__|    |_|  |_|_| |_| |_|\___|


---------------------------oOOo-------------------------
""", 'blue') # - Title Screen -
mainroom = colored("""
---------------------------oOOo-------------------------
 _______         |       _______        |       _______
|       |       (_)     |       |      (_)     |       |
|       |               |_______|              |       |
| o     |               {***|***}              | o     |
|       |               |       |              |       |
|   1   |_______________|   2   |______________|   3   |

---------------------------oOOo-------------------------
	""", 'blue') # - Main Room -
doorone = colored("""
---------------------------oOOo-------------------------
 _______      |            |        |     ____   ____
|       |    (_)          (_)       |    |    | |    |
|       |                           |    |____| |____|
| o     |               _________   |
|       |               |_______|   |
|   1   |_______________|   2   |___|     3 GO BACK >

---------------------------oOOo-------------------------
""", 'blue')
doorthree = colored("""
---------------------------oOOo-------------------------
__________         |       _______        |
          |       (_)     [       ]      (_)
          |               | .   . |
< GO BACk |               |       |           __
          |               | .   . |          |" |
    3     |______________ [   1   ]__________|2 |______

---------------------------oOOo-------------------------
""", 'blue')
doorfour = colored("""
---------------------------oOOo-------------------------
      |     |                 ______
     (_)    |                |   1  |
            |                |______|
< 2 GO BACK |              ___[++++]____      |
            |              |           |   ___|
            |______________|           |__|   |_________

---------------------------oOOo-------------------------
""", 'blue')
pc_terminal = colored("""
---------------------------oOOo-------------------------
         ________________________________________
        |   __________________________________   |
        |  |                                  |..|
        |..|                                  |  |
        |  |  C:\>_ disable_electric_door     |  |
        |O |                                  | O|
        |O |  C:\>_ crack_code                | O|
        |  |                                  |  |
        |  |  C:\>_ exit                      |  |
        |..|__________________________________|..|
        |________________________________________|
          [  + + + ++ + + + + + + + + + + + + ]
---------------------------oOOo-------------------------
""", 'blue')
pc_crackcode = colored("""
---------------------------oOOo-------------------------
         ________________________________________
        |   __________________________________   |
        |  |                                  |..|
        |..|         [_2]  [_3]  [_5]         |  |
        |  |         [_7]  [__]  [13]         |  |
        |O |         [17]  [19]  [23]         | O|
        |O |                                  | O|
        |  |                                  |  |
        |  |  C:\>_ exit                      |  |
        |..|__________________________________|..|
        |________________________________________|
          [  + + + ++ + + + + + + + + + + + + ]
---------------------------oOOo-------------------------
""", 'blue')
alive_robot = colored("""
---------------------------oOOo-------------------------
      |    \                ___|___       |       |
     (_)    |              | o   o |      (_)     (_)
            |              |___^___|
< 2 GO BACK |               [|. .|]
            |        1 >    ||___||
            |_________________| |______________________

---------------------------oOOo-------------------------
""", 'blue')
robot_art = alive_robot
death_robot = colored("""
---------------------------oOOo-------------------------
      |    \                              |       |
     (_)    |                            (_)     (_)
            |                  _____
< 2 GO BACK |                 |     |
            |                 |R.I.P|
            |_________________|     |___________________

---------------------------oOOo-------------------------
""", 'blue')
doortwo = colored("""
 __   __  _______  __   __    _     _  ___   __    _    __
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |  |  |
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |  |  |
|       ||  | |  ||  |_|  |  |       ||   | |       |  |  |
|_     _||  |_|  ||       |  |       ||   | |  _    |  |__|
  |   |  |       ||       |  |   _   ||   | | | |   |   __
  |___|  |_______||_______|  |__| |__||___| |_|  |__|  |__|

  created by Denis Matei 2018
""", 'blue')

# - VARIABLES -
lives = 3
items = []
key = "Key"
terminalpaper = "log_123"
first_code = "567"
second_code = "294"

# - Switches -
drawer = 1
trashbin = 1
electricdoor = 1
electricity = 1
crackcode = 1
robot = 1

# - MAPS -
def main_room():
	print mainroom
	print "I see three strange doors in front of me."
	print "Maybe I should try to open one."
	print "I think I will open..."

	answer = raw_input('-> ')

	if answer == "1": # < DOOR 1
		door_one()
	elif answer == "2": # < DOOR 2
		print "This door is different."
		print "It seems like it requires a password."
		print "Let's try..."

		password = raw_input('->')

		if password == "567294":
			print "-" * 56
			door_two()
		else:
			print "-" * 56
			print colored("Wrong Password!", 'red')
			global lives
			lives -= 1
			life_count()
			if lives != 0:
				main_room()


	elif answer == "3": # - DOOR 3 -
		door_three()

	elif answer == "status": # - SHOW LIVES & ITEMS -
		menu()
		print "Type Anything to Exit Status..."

		answer = raw_input("-> ")

		if answer == "abc":
			print "a is for apathy, b is for boos, c is for cunt."
			main_room()
		else:
			main_room()
	else:
		print "-" * 56
		print colored("Cannot Understand Command", 'red')
		print "Options are 1, 2, or 3."
		main_room()

def door_one():
	print doorone
	print "I see a door and a little drawer."
	print "It seems like the door is locked and dangerous."
	print "I think I'll explore..."

	answer = raw_input('-> ')

	if answer == "1":
		if "Key" in items:
			print 56 * "-"
			print "Used 'Key' on Door 4."
			door_four()
		else:
			print 56 * "-"
			print colored("You don't have 'Key'.", 'red')
			global lives
			lives -= 1
			life_count()
			if lives != 0:
				door_one()

	elif answer == "2":
		global drawer
		if drawer == 1:
			print 56 * "-"
			print colored("Found Key!", 'red')
			items.append(key)
			drawer += 1
			door_one()
		else:
			print 56 * "-"
			print colored("Drawer is empty.", 'red')
			door_one()

	elif answer == "3":
		main_room()

	elif answer == "status":
		menu()
		print "Type Anything to Exit Status..."

		answer = raw_input("-> ")

		if answer == "123":
			print "1 dead kitten, 2 dead penguins, 3 dead zombies."
			door_one()
		else:
			door_one()

	else:
		print "-" * 56
		print colored("Cannot Understand Command.", 'red')
		print "Options are 1, 2, or 3.\n"
		door_one()

def door_two():
	print doortwo

def door_three():
	print doorthree
	print "I see a little trashcan and some kind of electric door."
	print "I am going to explore..."

	answer = raw_input('->')

	if answer == "1":
		global electricdoor
		if electricdoor == 1:
			print "The door is emitting sparks of electricity."
			print "I don't think I should touch this door..."
			print "Open door?"
			print colored("\tyes", 'green'), "|", colored("no", 'red')

			answer = raw_input("-> ")

			if answer == "yes":
				print "-" * 56
				print colored("Got Electrocuted!", 'red')
				global lives
				lives -= 1
				life_count()
				if lives != 0:
					door_three()
			else:
				door_three()
		else:
			print "Electric door is safe to open."
			electric_door()


	elif answer == "2":
		global trashbin
		if trashbin == 1:
			print 56 * "-"
			print colored("Found a piece of paper!", 'red')
			print colored("It says 'log_123'", 'red')
			items.append(terminalpaper)
			trashbin += 1
			door_three()
		else:
			print 56 * "-"
			print colored("Trashbin is empty.", 'red')
			door_three()


	elif answer == "3":
		main_room()

	elif answer == "status":
		menu()
		print "Type Anything to Exit Status..."

		answer = raw_input("-> ")

		if answer == "fuckyou":
			print "and... fuck you too :)"
			door_three()
		else:
			door_three()

	else:
		print "-" * 56
		print colored("Cannot Understand Command.", 'red')
		print "Options are 1, 2, or 3.\n"
		door_three()

def door_four():
	print doorfour
	print "This room is pretty empty aside from that Terminal."
	print "I will explore..."

	answer = raw_input('-> ')
	if answer == "1":
		print "Enter Terminal Password."
		password = raw_input('->')

		if password == "log_123":
			terminal()
		else:
			print 56 * "-"
			print colored("Wrong Terminal Pasword.", 'red')
			print "I need to find the Terminal Pasword."
			global lives
			lives -= 1
			life_count()
			if lives != 0:
				door_four()

	elif answer == "status":
		menu()
		print "Type Anything to Exit Status..."

		answer = raw_input("-> ")

		if answer == "123":
			print "1 dead kitten, 2 dead penguins, 3 dead zombies."
			door_four()
		else:
			door_four()

	elif answer == "2":
		door_one()
	else:
		print "-" * 56
		print colored("Cannot understand command.", 'red')
		print "Options are 1 or 2.\n"
		door_four()

def terminal():
	print pc_terminal
	print "Seems like I have a few options on this Terminal."
	print "I will go for..."

	option = raw_input('>_')

	if option == "disable_electric_door":
		global electricity
		if electricity == 1:
			print "-" * 56
			print "Electricity disabled."

			electricity += 1

			global electricdoor
			electricdoor += 1
			terminal()
		else:
			print "-" * 56
			print "Already disabled."
			terminal()

	elif option == "crack_code":
		terminal_crack_code()

	elif option == "exit":
		door_four()

	elif option == "kill_robot":
		print colored("Robot Has Been Killed.", 'red')
		global robot_art
		robot_art = death_robot
		terminal()

	else:
		print "-" * 56
		print colored("Cannot understand command.", 'red')
		print "Options are disable_electric_door."
		print "Or crack_code. \n"
		terminal()

def terminal_crack_code():
	print pc_crackcode
	print "Looks like a matrix puzzle."
	print "The number in the middle is missing."
	print "I think the number should be..."

	number = raw_input('>_')

	if number == "11":
		global crackcode
		if crackcode == 1:
			print 56 * "-"
			print ">_PRIME NUMBER IDENTIFIED"
			print "The Terminal is printing something."
			print "Oh look! A piece of paper with a code!"
			print colored("Found piece of paper '567'.", 'red')
			crackcode += 1
			items.append(first_code)
			terminal()
		else:
			print 56 * "-"
			print "Out of Paper..."
			terminal()

	elif number == "exit":
		terminal()

	else:
		print 56 * "-"
		print colored("Wrong Answer!", 'red')
		print "It seems like a well-known number seqeunce."
		global lives
		lives -= 1
		life_count()
		if lives != 0:
			terminal_crack_code()

def electric_door():
	print robot_art
	print "Oh look! A weird Robot with nipples!"
	print "Man, the developer must be really messed up..."
	print "Will I go back or talk it..."

	answer = raw_input('->')

	if answer == "1":
		global robot
		if robot == 1:
			print 56 * "-"
			print colored("""
 /`-.__                                 /\\
 `. .  ~~--..__                   __..-' ,'
   `.`-.._     ~~---...___...---~~  _,~,/
     `-._ ~--..__             __..-~ _-~
         ~~-..__ ~~--.....--~~   _.-~
                ~~--...___...--~~


			""", 'yellow')
			print "Bana Is A Berry....BIB!?"
			print colored("\tyes", 'green'), "|", colored("no", 'red')

			answer = raw_input("-> ")

			if answer == "yes":
				print 56 * "-"
				print "You Are Correct ... BIB!"
				print "The messed up Robot is satisfied with my answer."
				print "It is giving me a piece of paper!"
				print colored("Found piece of paper '294'.", 'red')
				robot += 1
				items.append(second_code)
				electric_door()

			elif answer == "no":
				print 56 * "-"
				print colored("WRONG!", 'red')
				webbrowser.open(
					'https://www.livescience.com/57477-why-are-bananas'
					'-considered-berries.html')
				global lives
				lives -= 1
				life_count()
				if lives != 0:
					electric_door()

			else:
				print "-" * 56
				print colored("Cannot understand command.", 'red')
				print "Options are yes or no. \n"
				electric_door()


		else:
			print "-" * 56
			print "BIB &*&$ bib%%% bB$^3@&$@*$&("
			print " @@&$*F$#()U*)_)_CK$"
			print " ...YOU! bib bib bib ___&%&%&%&\n"
			print "I wonder if I can kill this Robot with the Terminal."
			electric_door()


	elif answer == "2":
		door_three()


	elif answer == "status": # - SHOW LIVES & ITEMS -
		menu()
		print "Type Anything to Exit Status..."

		answer = raw_input("-> ")

		if answer == "abc":
			print "a is for apathy, b is for boos, c is for cunt."
			electric_door()
		else:
			electric_door()

	else:
		print "-" * 56
		print colored("Cannot understand command.", 'red')
		print "Options are 1 or 2. \n"
		electric_door()


# - STATES -
def life_count():
	global lives
	if lives == 3:
		print colored("Lives Left [o][o][o]", 'blue')
	elif lives == 2:
		print colored("Lives Left [X][o][o]", 'blue')
	elif lives == 1:
		print colored("Lives Left [X][X][o]", 'blue')
	elif lives == 0:
		print colored("Lives Left [X][X][X]", 'blue')
		print colored("You Died.", 'red')
		exit(0)
	else:
		print"DO NOTHING..."

def menu():
	print colored("""
---------------------------oOOo-------------------------
	""", 'blue')
	life_count()
	print colored("Items Collected", 'blue'), items
	print colored("""
---------------------------oOOo-------------------------
		\n""", 'blue')

def start_screen():
	print title
	print "Welcome to Quest Time!"
	print "Would you like to Start?"
	print colored("\tyes", 'green'), "|", colored("no", 'red')
	answer = raw_input("-> ")
	if answer == "yes":
		print colored("Starting Game...", 'green')
		print "-" * 56
		print "To See Your Items & Lives Type:"
		print colored("\tstatus\n", 'green')
		main_room()
	elif answer == "no":
		print colored("Closing Game...", 'red')
		exit(0)
	else:
		print "-" * 56
		print colored("Cannot understand command.", 'red')
		print "Options are (yes) and (no).\n"
		start_screen()

# - Starts Game -
start_screen()
