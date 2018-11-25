"""
Code that will calculate the cheapest way of shipping packages based on their
weight. Options are Premium shipping, ground shipping, and Drone shipping.
"""

print # for tab

# Normal ground shipping:
def ground_shipping(weight):
    cost = 20
    if weight <= 2:
        cost += weight * 1.50

    elif weight > 2 and weight <= 6:
        cost += weight * 3.00

    elif weight > 6 and weight <= 10:
        cost += weight * 4.00

    elif weight > 10:
        cost += weight * 4.75

    return cost


# Drone shipping:
def drone_shipping(weight):
    cost = 0
    if weight <= 2:
        cost += weight * 4.50

    elif weight > 2 and weight <= 6:
        cost += weight * 9.00

    elif weight > 6 and weight <= 10:
        cost += weight * 12.00

    elif weight > 10:
        cost += weight * 14.25

    return cost


# Cheapest shipping:
def cheapest_shipping(weight):

    method_1 = 125.0                     # This is simply the premium ground shipping
    method_2 = ground_shipping(weight)   # ground shipping as we know it.
    method_3 = drone_shipping(weight)    # drone shipping.


    if method_1 < method_2 and method_1 < method_3:
        print("Premium ground shipping is the cheapest at ${}\n".format(
            method_1))


    elif method_2 < method_1 and method_2 < method_3:
        print("Regular ground shipping is the cheapest at ${}\n".format(
            method_2))

    elif method_3 < method_1 and method_3 < method_2:
        print("Drone shipping is the cheapest at ${}\n".format(method_3))


# Function call:
cheapest_shipping(4.8)
cheapest_shipping(41.5)
cheapest_shipping(12)
cheapest_shipping(5)
cheapest_shipping(92)
