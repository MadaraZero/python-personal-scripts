# The Pig Latin app adds the first letter of a word to the end of the word
# and then adds 'ay' at the end of the word.
pyg = 'ay'

# Where the user inputs the word.
original = raw_input('Enter a word:')

# If the lenght of the 'word' is greater than 0 characters 'and'...
# the 'word' contains 'no-numbers' the 'if statement' is satisified.
if len(original) > 0 and original.isalpha():
    # a variable that turns the user's input into a lowercase word.
    word = original.lower()
    # a variable that gets the first letter of a word.
    first = word[0]
    # a variable that combines the previous variables.
    new_word = word + first + pyg
    # takes the new word and puts it before the second letter.
    new_word = new_word[1:len(new_word)]
    # print the result of the variables and if statement.
    print new_word
else:
    print 'empty'


# new_word = new_word[1:len(new_word)] this variables makes sure to print the
# result of (word + first + pyg) by starting with the second
# letter of the result. Or else you would get, for example,
# denis --> 'd'enisday instead of enisday.

def selection():
	gold = check_int(raw_input(">>> "))
	# gold = raw_input(">>> ")
	# check_int(gold)
	if gold == True:
		print "That is a number %d" % gold
	else:
		print "NO NUMBER"
