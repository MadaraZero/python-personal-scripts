"""
Script that allows an user to read a text file.
"""

# Filereader:
from sys import argv

script, filename = argv

print "Do you want to read %r?" % filename
print "Yes|No?"
read_file = raw_input("> ")
if read_file == "Yes":
    target = open(filename, 'r')
    print target.read()
else:
    print "Process Has Been Terminated"


# Multiple Filereader:
from sys import argv

script, filename, filename_2 , filename_3 = argv

print "Do you want to read %r, %r, and %r?" % (filename, filename_2, filename_3)
print "Yes|No?"
read_file = raw_input("> ")
if read_file == "Yes":
    target_1 = open(filename, 'r')
    print target_1.read()
    target_2 = open(filename_2, 'r')
    print target_2.read()
    target_3 = open(filename_3, 'r')
    print target_3.read()
else:
    print "Process Has Been Terminated"

# multiple_filereader.py test.txt test_2.txt test_3.txt
