# python AreaCalculator.py
""" 
AreaCalculator calculates the surface area of a Circle or a Triangle.
"""

def auto_calculator():
    print  # for space
    print "Welcome to AutoCalculator!\n"
    option = raw_input("Enter C for Circle or T for Triangle: ")
    option = option.lower()

    if option == 'c':
        print '=' * 35
        radius = float(raw_input("Circle radius: "))
        area = 3.14159 * radius ** 2
        print "Circle surface area: %d" % area
        print '=' * 35

    elif option == 't':
        print '=' * 35
        base = float(raw_input("Triangle base: "))
        height = float(raw_input("Triangle height: "))
        area = base * height / 2
        print "Triangle surface area: %d" % area
        print '=' * 35

    else:
        print "That is not a valid input."
        auto_calculator()


auto_calculator()
print "Exiting AutoCalculator..."
exit()

