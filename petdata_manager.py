"""
Pet data register:
- Register pet data
- And retrieve specific pet Data
- Retrieve all Pet data
"""
# CLASSES:

# Pet class.
class Pet(object):
    def __init__(self, petname, species, age, owner):

        self.petname = petname
        self.species = species
        self.age = age
        self.owner = owner

    def __str__(self):
        return """
----------------------------
Pet Name: %s\nSpecies: %s\nAge: %s\nOwnner: %s
----------------------------
        """ % (self.petname, self.species, self.age, self.owner)


# DICTIONARIES:

# Dictionary with the pet name and pet ID number.
pet_id = {}
# All pet data stored here.
pet_data = {}

# FUNCTIONS:
# Register a new pet.
def pet_object_creator():

    a = raw_input('Petname: ')            # Petname is also dictionary value.
    b = raw_input('Species: ')
    c = int(raw_input('Age: '))
    d = raw_input('Owner Name: ')

    dict_val = a                          # The value name is the Petname.
    pet_info = Pet(a, b, c, d)            # Creating the Pet object.

    dict_key = int(raw_input('Pet ID: ')) # Pet ID is also dictionary key.

    pet_id[dict_key] = dict_val           # Store (dict_key, dict_val) in pet_id
    pet_data[dict_val] = pet_info         # Store user input info in pet_data

    menu()

# Acces pet data.
def acces_pet_data():
    for key, val in pet_id.items():
        print '| ID: %s  | Name: %s' % (key, val)

    print # for space
    print "Type ID of pet to see its data."
    print "Type '0' to go back.\n"

    input = int(raw_input('> '))

    if input in pet_id:
        for key in pet_id:
            if key == input:
                print pet_data[pet_id[key]]
                menu()

    elif input == 0:
        menu()

    else:
        print # for space
        print "There is no data stored with ID number %r.\n" % input
        acces_pet_data()

# Delete pet data.
def delete_pet_data():

    for key, val in pet_id.items():
        print '| ID: %s | Name: %s' % (key, val)

    print # for space
    print "Type ID of pet to delete it.."
    print "Type '0' to go back.\n"

    input = int(raw_input('> '))

    if input in pet_id:
        for key in pet_id:
            if key == input:
                del pet_id[key]
                menu()

    elif input == 0:
        menu()

    else:
        print # for space
        print "There is no data stored with ID number %r.\n" % input
        deleted_pet_data()

# Acces deleted pet data.
def deleted_pet_data():
    for key, val in pet_data.items():
        print "Removed Pet ID %s" % key
        print val
    menu()

# Menu of the Pet Data Manager.
def menu():
    print # for space
    print "Welcome to Pet Data Manager!\n"
    print "> Register new pet     1"
    print "> Acces pet data       2"
    print "> Delete pet data      3"
    print "> Acces all data       4\n"
    user_input = raw_input('> ')

    if user_input == '1':
        print # for space
        pet_object_creator()

    elif user_input == '2':
        print # for space
        acces_pet_data()

    elif user_input == '3':
        print # for space
        delete_pet_data()

    elif user_input == '4':
        deleted_pet_data()

    elif user_input == 'exit':
        exit()

    else:
        print "That is not a valid keyboard input."
        menu()

menu()
