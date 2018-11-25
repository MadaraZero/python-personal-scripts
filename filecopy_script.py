"""
Script that copies text from a text file to another text file.
"""

from sys import argv

script, from_file, to_file = argv

print "Would you like to copy text from %s to %s?" % (from_file, to_file)
print "Yes|No?"
file_copy = raw_input('> ')
if file_copy == "Yes":
    in_file = open(from_file); indata = in_file.read()
    out_file = open(to_file, 'w')
    out_file.write(indata)
    print "File Has Been Copied"
    out_file.close()
    in_file.close()
else:
    print "Process Aborted"
    out_file.close()
    in_file.close()
