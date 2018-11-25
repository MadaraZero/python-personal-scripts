"""
Code that calculates the total score of a player that has played scrable
based on the words he used in the game.
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1,
          4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}


    # Creating a dictionary through dictionary comprehension:
letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0


    # Function that returns sum of points based on a word:
def score_words(word):
    point_total = 0
    for letter in word:
        if letter in letter_to_points:
            point_total += letter_to_points[letter]

    return point_total




    # Dictionary of players and the words they used:
player_to_words = {
    "player1": ["BLUE", "TENNIS", "TENNIS"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "ProfReader": ["ZAP", "COMA", "PERIOD"]
}

    # Dictionary for saving the player as key and score as value:
player_to_points = {}

    # Loop to fill in the 'players_to_points' dictionary:
for key, words in player_to_words.items():
    players_points = 0
    for word in words:
        players_points += score_words(word)
    player_to_points[key] = players_points

print(player_to_points)
