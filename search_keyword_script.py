"""
Searching script that searches a specific keyword in a txt file.
"""

def search(keyword, filename):

    print('generator started')
    f = open(filename, 'r')

    # Looping through the file line by line.
    for line in f:
        if keyword in line:

            # If keyword found, return it.
            yield line
    f.close()

the_generator = search("LLEN", 'test2.txt')
print(the_generator.next())
