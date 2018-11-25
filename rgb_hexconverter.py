"""
This program allows an user to convert RGB to Hex and vice-versa.
"""

from time import sleep
from termcolor import colored as clrd


def rgb_hex():
    invalid_msg = "Value has to be between 0 and 255."

    red = int(raw_input("Enter red (R) value: "))
    if red < 0 or red > 255:
        print invalid_msg
        return

    green = int(raw_input("Enter green (G) value: "))
    if green < 0 or green > 255:
        print invalid_msg
        return

    blue = int(raw_input("Enter blue (B) value: "))
    if blue < 0 or blue > 255:
        print invalid_msg
        return

    val = (red << 16) + (green << 8) + blue
    print "Computer is calculating..."
    sleep(2)
    print "%s \n" % (hex(val)[2:]).upper()


def hex_rgb():
    hex_val = raw_input("Enter hex value: ")
    if len(hex_val) != 6:
        print "Hex value has to be 6 characters long."
        return
    else:
        hex_val = int(hex_val, 16)

    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8

    red = hex_val % two_hex_digits
    # hex_val = hex_val >> 8

    print "Computer is calculating..."
    sleep(2)
    print clrd("Red: %s |",'red') % red, clrd("Green: %s |",'green') % green, \
        clrd("Blue: %s\n",'blue') % blue


def convert():
    while True:
        print "Enter 1 to convert RGB > HEX."
        print "Enter 2 to convert HEX > RGB."
        print "Enter X to exit program.\n"
        option = raw_input("Enter choice: ")
        option = option.upper()

        if option == '1':
            print "RGB to Hex..."
            rgb_hex()
        elif option == '2':
            print "Hex to RGB..."
            hex_rgb()
        elif option == 'X':
            break
        else:
            print "No such option."
            convert()


convert()
