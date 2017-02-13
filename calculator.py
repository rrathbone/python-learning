"""Python is especially useful for doing math and can be used to automate many calculations. In this project, you'll create a calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle
The program should do the following:

Prompt the user to select a shape
Depending on the shape the user selects, calculate the area of that shape
Print the area of that shape to the user"""

from math import pi
from time import sleep
from datetime import datetime

#.now() is accessing the now content from the imported datetime module
now = datetime.now()

print 'Starting the calculator...'
print '%s-%s-%s' % (now.year, now.month, now.day)

sleep(1)

hint = 'Don\'t forget to include the correct units! \nExiting...'

option = raw_input('Enter C for Circle or T for Triangle: ').upper()

if option == 'C':
    radius = float(raw_input("Enter radius: "))
    area = pi * radius**2
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = (0.5)*base*height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
else:
	print 'You entered garbage so the program will now exit.'
