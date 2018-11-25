"""
Organizing a business through the use of classes.
"""

# Menu dictionaries:
arepas_menu = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}

earlybird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}

dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}

kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}


# Menu class:
class Menu:
    # init variables:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # representation when using the print method on the class:
    def __repr__(self):
        return "{} menu available from {} to {}".format(self.name,
                                                        self.start_time,
                                                        self.end_time)

    # a class method to calculate the bill of a customer:
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]

        return total


# Menu instances:
brunch = Menu("Brunch", brunch_items, "11am", "4pm")
early_bird = Menu("Early-Bird", earlybird_items, "3pm", "6pm")
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")
kids = Menu("Kids", kids_items, "11am", "9pm")


# Calculating price of a customer:
bill_1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
bill_2 = early_bird.calculate_bill(
    ['salumeria plate', 'mushroom ravioli (vegan)'])


# Franchise class:
class Franchise:
    def __init__(self, adress, menus):
        self.adress = adress
        self.menus = menus

    def __repr__(self):
        return "Restaurant Adress: {}".format(self.adress)

# ============================================================================x
    def available_menus(self, time):
        lst = []
        if time == "11am":
            lst.append(brunch)
            lst.append(kids)
        elif time == "5pm":
            lst.append(dinner)
        elif time == "3pm":
            lst.append(early_bird)
        else:
            return "Invalid time."
        return lst


# Franchise instances:
flagship_store = Franchise("1232 West End Road",
                           [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street",
                            [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# ============================================================================X
# Point of improvement is fixing the logic for the time:
lol = flagship_store.available_menus("11am")
# print(lol)


# Business class:
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Business instances:
business_1 = Business("Basta Fazoolin' with my Heart",
                      [flagship_store, new_installment])
business_2 = Business("Take a' Arepa", [arepas_place])
