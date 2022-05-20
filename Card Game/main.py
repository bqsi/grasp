"""

'Card Game' is part of 2 repls I made today (25/04) to work with file reading as well as other forms of logic.

They're pretty generic games as far as it goes.

Nested arrays are always fun and this one is no exception.

"""

# - Initial Vars and Introduction - #

import random

# Cards and round number
cards = []
rn = 0

# FYI, this entire section of file reading is taken from music game (https://replit.com/@bqsi/Music-Game) since they both use the exact same logic
# It's just adapted for this code

# Open the scores.txt file for reading and declare scorestable
scores = open("scores.txt", "r")
scorestable = []

# Sort function for below
def sortFunc(x):
  return x[1]

# Interpret and assign scores to a table:
# Take what is in the scores file already - it's all in the same format, so:
# use str.split to split it into two things, a name and a number
# Convert the number into an int since it was previously a string
# Sort the table according to the sort function above (which returns the score as a key)
for x in scores:
  scorestable.append([x.split(" ")[0], int(x.split(" ")[1])])
  scorestable.sort(reverse=True, key=sortFunc)
scores.close()

# Assign the cards their values and make sure they're unique (i'm not typing out the entire table)
c = ["black", "red", "yellow"]
for i in range(0,3):
  for x in range(1,11):
    cards.append([c[i], x])

# Authentication stuff
auth = ['sam', 'craig', 'liam']

# Name, points, inventory.
p1Name, p2Name = "", ""
p1Points, p2Points = 0, 0
p1Inventory, p2Inventory = [], []

# - Functions - #

# Auth a player's input for their name against the auth table
def playerAuthenticated(inp):
  return inp.lower() in auth

# Simple shorthand for shuffling the deck
def shuffleDeck(deck):
  random.shuffle(deck)
  return deck

def decideWinner(p1, p2):
  if p1[0] == p2[0]:
    if max(p1[1], p2[1]) == p1[1]:
      return p1
    else:
      return p2
  if p1[0] == 'red':
    return p2[0] == 'black' and p1 or p2
  if p1[0] == 'yellow':
    return p2[0] == 'red' and p1 or p2
  return p2[0] == 'yellow' and p1 or p2


# Function to play the round. Takes a lot of vars for returning later on:
# Player 1's current points and inventory, same for player 2, + the round number and the current deck
def playRound(p1p, p2p, p1i, p2i, rn, deck):
  print(f"Round {rn}.")
  input("Press enter to continue. ")
  print(f"There are currently {len(deck)} cards in the deck.")

  # Shuffle the deck and give each player the top card off the deck.
  deck = shuffleDeck(deck)
  print("The deck has been shuffled.")
  print("Both players are taking their cards..")
  print()

  # Next, take the card which each player has out of the original deck.
  p1Take, p2Take = deck[0], deck[1]
  print("Player one takes a card..\n")
  deck.pop(deck.index(p1Take))
  print("Player two takes a card..\n")
  deck.pop(deck.index(p2Take))

  # Print what each player had.
  print(f"Player 1 got a {p1Take[0].title()} card with the number {p1Take[1]}.")
  print(f"Player 2 got a {p2Take[0].title()} card with the number {p2Take[1]}.")

  # Simple win logic.
  # If either player takes the round based on the logic in decideWinner,
  # add both of the cards to the player's "inventory" and display a win message + their current points.
  if decideWinner(p1Take, p2Take) == p1Take:
    p1p += 1
    p1i.append(p1Take)
    p1i.append(p2Take)
    print(f"Player 1 wins this round! They have {p1p} points.")
  else:
    p2p += 1
    p2i.append(p1Take)
    p2i.append(p2Take)
    print(f"Player 2 wins this round! They have {p2p} points.")

  return p1p, p2p, p1i, p2i, deck

# Do the auth stuff, raise exceptions if anything's amiss
p1Name = input("Player 1, please enter your name. Only authenticated users can play this game. ").title()
p2Name = input("Player 2, please enter your name. Only authenticated users can play this game. ").title()
if p1Name == p2Name: raise Exception("Player names must be different.")
if not playerAuthenticated(p1Name) or not playerAuthenticated(p2Name): raise Exception("A player is not authenticated.")

# Honestly, the workflow for this is kind of messy, but bear with me.
# All of the vars being assigned are returned on the last line of playRound.
# It's not terrible, but it's just how I came up with doing it.
# While there's still cards in the deck, just keep playing rounds.
while len(cards) > 0:
  # The thing is that if I wanted to keep all of the round logic condensed into one function, I'd likely end up doing this but just more longform if I used more than one function.
  # This is just what my brain came up with at the time.
  rn += 1
  p1Points, p2Points, p1Inventory, p2Inventory, cards = playRound(p1Points, p2Points, p1Inventory, p2Inventory, rn, cards)
  # Only reason this really looks messy is because of the var names lol

# Ending message, winner logic, yada yada (i don't like commenting this code anymore, too tired)
print("The game has ended as the deck is now empty.")
print(f"The winner is {(p1Points > p2Points) and p1Name or p2Name} with {(p1Points > p2Points) and len(p1Inventory) or len(p2Inventory)} cards.")

# Write the player's name to the scores table we made earlier
print("Your score will be written to an external file. Here are the top 5 scores!")
scorestable.append([(p1Points > p2Points) and p1Name or p2Name + ":", (p1Points > p2Points) and len(p1Inventory) or len(p2Inventory)])
scorestable.sort(reverse=True, key=sortFunc)

# For each element of scores table, write a new line in scores.txt of that score
scores = open("scores.txt", "w")
for i in scorestable:
  scores.write(f"{i[0]}: {i[1]}\n")

# Print the top 5 scores (or if there's not 5 scores, just the entire list)
for i in range(0,(len(scorestable) >= 5 and 5 or len(scorestable))):
  print(f"{scorestable[i][0]} {scorestable[i][1]}")

# Close the file to prevent buffers from killing our previous inputs
scores.close()
