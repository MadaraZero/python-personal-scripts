## — My Store — ##
# dictionary with prices of the fruit keys
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# dictionary with the stock of the fruit keys
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

# list of the items ordered by a person
shopping_list = ["banana", "orange", "apple"]

# Gives us an organized overview of our stock and prices:
for food in prices:
  print food
  print "price %s" % prices[food]
  print "stock %s" % stock[food]
  print # gives nice spacing i.e. more overview

# calculates the total networth of the store which is 117.0
total = 0
for food in prices:
  print "Networth of " + food +'\'s'
  print prices[food] * stock[food]
  total = total + prices[food] * stock[food]
  print # gives nice spacing i.e. more overview
print "Total Networth: %s" % total

# function: Calculates the contents of checkout from a person.
# if the stock is above 0 add the price to the total of checkout.
# after that deduct one item from the stock(because it is bought!)
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total
print "Checkout Price: %s" % compute_bill(shopping_list)
