"""
Filewriter 2.1
A script that allows an user to write text to a txt file.
"""

# Update Notes: Added space before first written character on any line.
from sys import argv

script, filename = argv

n = 0
n_string = str(n) + " "
writing = None

print # Used 'print' to create more overview in the terminal.
print "------------------------< Session Started >------------------------"
print
print "\t > Welcome to Filewriter 2.1!"
print "\t > update notes :: spacing before character ::"
print "\t > In this program you can create your own text file."
print "\t > to stop writing, write the secret key word: "
print "\t > STOP "
print "\t > Would you like to now write a file?"
print "\t Yes | No?"
start = raw_input('> ')
if start == "Yes":
	print "\t > Write a line:"
	target = open(filename, 'w')
	while writing != "STOP":
		writing = raw_input(n_string) # write a line
		target.write(writing)
		target.write("\n")
		n += 1
		str(n)
		n_string = str(n) + " "
else:
	print "\t > File Writing Has Been Aborted"
	print
	print "------------------------< Session Ended >------------------------"
	target = open(filename)
	target.close()
	exit()

print "\t > File Has Been Written"
print
print "\t > Would you like to read the %r file?" % filename
print "\t Yes | No?"
read_file = raw_input('> ')
if read_file == "Yes":
	target = open(filename, 'r')
	print target.read()
	target.close()
	print "------------------------< Session Ended >------------------------"
else:
	print "\t > File Writing Has Been Completed"
	target = open(filename)
	target.close()
	print
	print "------------------------< Session Ended >------------------------"
