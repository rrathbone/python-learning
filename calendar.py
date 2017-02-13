 """So far, you've used Python to build a variety of things, including calculators and games. In this project, we'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
The program should behave in the following way:

Print a welcome message to the user
Prompt the user to view, add, update, or delete an event on the calendar
Depending on the user's input: view, add, update, or delete an event on the calendar
The program should never terminate unless the user decides to exit
Let's begin!"""

from time import sleep, strftime

FIRST_NAME = "Rachelle"
calendar = {}


def welcome():
    print "Welcome " + FIRST_NAME
    print "The calendar is opening..."
    sleep(1)
    print "Today is: " + strftime("%A %B %d, %Y")
    print "The current time is: " + strftime("%H:%M:%S")
    print "What would you like to do?"


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()

    if user_choice == "V":
        if len(calendar.keys()) < 1:
            print "Calendar is empty."
        else:
            print calendar

    elif user_choice == "U":
        date = raw_input("What date? ")
        update = raw_input("Enter the update: ")
        calendar[date] = update
        print calendar

    elif user_choice == "A":
        event = raw_input("Enter event: ")
        date = raw_input("Enter date (MM/DD/YYYY): ")
        if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
            print "Invalid date entered"
            try_again = raw_input("Try Again? Y for Yes, N for No: ")
            try_again = try_again.upper()
        if try_again == "Y":
            continue
        else:
            start = False
      else:
          calendar[date] = event
          print "Event added"
          print calendar

    elif user_choice == "D":
        if len(calendar.keys()) < 1:
            print "Calendar is empty."
      else:
        event = raw_input("What event? ")
        if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
            print calendar
        else:
            print "Incorrect event entered"

    elif user_choice == "X":
        start = False

    else:
        print "Invalid command entered"
        start = False

start_calendar()
