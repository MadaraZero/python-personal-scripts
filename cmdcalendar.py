"""
This is a calendar program that will be used through command lines.
The user can view, add, update, or delete an event on the calendar.
The program only closes after the user wishes to.
"""

print # for tab
from time import sleep, strftime
from termcolor import colored as clrd
import pprint

NAME = "Denis Matei"
calendar = {} # dates are used as keys.

def welcome():
  print "Welcome" + NAME + "."
  print "Calendar opening...\n"
  sleep(1)
  print "Today is: " + strftime(clrd("%A %B %d, %Y",'blue'))
  print "Current time is: " + strftime(clrd("%H:%M:%S\n",'blue'))
  print "What would you like to do?"


def start_calendar():
    welcome()
    start = True
    while start:
        print
        print "-Enter", clrd('A', 'green'), "to Add"
        print "-Enter", clrd('U', 'green'), "to Update"
        print "-Enter", clrd('V', 'green'), "to View"
        print "-Enter", clrd('D', 'green'), "to Delete"
        print "-Enter", clrd('X', 'red'), "to Exit"
        user_choice = raw_input("Enter your choice: ")
        user_choice = user_choice.upper()
        print # for tab
        ### Viewing the calendar
        if user_choice == 'V':
            if len(calendar.keys()) == 0:
                print clrd("Calendar is empty...",'red')
            else:
                for date, event in calendar.items():
                    print "Date: %s" % date
                    print "Event: %s" % event
                    print  # for tab

        ### Updating the calendar
        elif user_choice == 'U':
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print # for tab
            print clrd("Update succesful!",'green')
            for date, event in calendar.items():
                print "Date: %s" % date
                print "Event: %s" % event
                print # for tab

        ### Adding to the calendar
        elif user_choice == 'A':
            event = raw_input("Enter event: ")
            date = raw_input("Enter data (MM/DD/YYYY): ")

            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print clrd("Invalid date...",'red')
                print "-Enter Y for Yes"
                print "-Enter N for No"
                try_again = raw_input("Try again? ")
                try_again = try_again.upper()

                if try_again == 'Y':
                    continue
                else:
                    start = False

            else:
                calendar[date] = event
                print clrd("Event succesfully added!\n",'green')
                for date, event in calendar.items():
                    print "Date: %s" % date
                    print "Event: %s" % event
                    print  # for tab

        ### Deleting from the calendar
        elif user_choice == 'D':
            if len(calendar.keys()) == 0:
                print clrd("Calendar is empty...",'red')

            else:
                event = raw_input("What event?")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print clrd("Event succesfully deleted!",'green')
                        for date, event in calendar.items():
                            print "Date: %s" % date
                            print "Event: %s" % event
                            print  # for tab
                    else:
                        print "No such event found."

        ### Closing calendar
        elif user_choice == 'X':
            print clrd("Closing...",'red')
            sleep(2)
            start = False

        else:
            print clrd("Invalid command...", 'red')
            continue
            # print "Invalid command..."
            # print clrd("Closing...",'red')
            # sleep(2)
            # start = False


start_calendar()

