"""
The Boredless Tourist Engine is an engine intended to match tourists with
travel destinations based on their interests.
"""

print # for tab

	# Data lists:
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA",
               "Sao Paulo, Brazil", "Cairo, Egypt"]
attractions = [[] for d in destinations]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

	# Get index of destinition in the destinations list:
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index


	# Get traveler location:
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


	# Adding attractions to destination:
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
      return

  # Adding attractions:
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

	# Finding the best places for our travelers:
def find_attractions(destination, interests):

  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interests = []

  for possible_attraction in attractions_in_city:
    attraction_tags = possible_attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interests.append(possible_attraction[0])

  return attractions_with_interests


	# Finding attractions for travelers:
def get_attractions_for_traveler(traveler):
  interests_string = "Hi "
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,
                                          traveler_interests)
  interests_string = interests_string + traveler[0]
  interests_string = interests_string + ", we think you'll like these " \
                                        "places around "
  interests_string = interests_string + traveler[1] + ": "

  for i in traveler_attractions:
    interests_string = interests_string + i + ", "

  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France',
                                              ['monument']])
print(smills_france)
