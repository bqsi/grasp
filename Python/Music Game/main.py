"""

'Music Game' is part of 2 repls I made today (25/04) to work with file reading as well as other forms of logic.

I REALLY enjoyed working out the file reading logic for setting scores and what not.
It's freakishly simple but the concept took my head a lot longer to get around to this time.

They're pretty generic games as far as it goes, hence why musicInfo.py literally only has 2 song entries and score.txt is empty.

If you wanna play this game, go ahead, but the functionality is limited due to there only being 2 song entries. I advise you just look through the code. scores.txt *should* write, so I can check back on this and see new scores.

"""

# - Initial Vars - #

import random

# To see how the musicInfo dictionary works, see the file below this one (musicInfo.py)
from musicInfo import *

# Authentication list
auth = ['sam', 'craig', 'liam']

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

playerName = ""

state = ""
points = 0
qN = 0

# - Functions - #

# Auth a player's input for their name against the auth table
def playerAuthenticated(inp):
  return inp.lower() in auth

# Decide the points based on logic surrounding the amount of guesses it took the user
def decidePoints(points, g):
  return (g == 1) and 3 or (g == 2) and 1 or "Fail"

# Decide a random song and artist and ask the user to guess them
# Pass the points argument as well as the question number to edit later on
def askQuestion(p, qn):
  # Declare a random int to make sure that the song and artist choice is the same
  ri = random.randint(0, len(musicInfo["songs"])-1)

  # Decide the random song and its corresponding artist
  song = musicInfo["songs"][ri]
  artist = musicInfo["artists"][ri]

  # Ask the question to the user using
  # the first letter of the song name + the artist.
  print(f"Question {qn}:")
  print(f"Guess the song name from the first letter of the song name and artist name:")
  print()
  print(f"Song Name 1st Letter: {song[0]}")
  print(f"Artist Name: {artist}")
  print()
  
  # Initialise guesses + an input
  guesses = 0
  guess = ""

  # While the user has more than 1 guess left..
  # Increment guesses, take their input
  # If it isn't equal to the song name, tell them how many guesses they have left
  # If it is equal, add points based on the decidePoints function and then
  # send back the correct state and the user's points for assignment
  # Otherwise, just send back the incorrect state and the user's current points
  while guesses != 2:
    guesses += 1
    guess = input()
    if guess.lower() != song.lower(): print(f"Incorrect. You have {2-guesses} guess(es) left.")
    if guess.lower() == song.lower():
      p += decidePoints(p, guesses)
      return "Correct", p
  return "Incorrect", p

# Do authentication stuff
playerName = input("Please enter your name. Only authenticated players may play this game. ")
if not playerAuthenticated(playerName):
  raise Exception("You are not authorised to play this game.")

# Print message for rules
print("Welcome to the song guessing game!")
print()
print("You will be presented with the first letter of a random song name and the artist's full name.")
print("You will have two tries to get the song name correct, otherwise the game will end.")
print()
input("Press enter to start. ")

# While there's a game going on..
# A state and points will be assigned by what the askQuestion function returns
# Pass it the player's current points and a question number
# Every time a question finishes, if it's correct, let them continue
# otherwise, break out of the game and go to the end protocols
while True:
  qN += 1

  state, points = askQuestion(points, qN)

  if state == "Correct":
    input("Correct! Press enter to continue. ")
  else:
    print("You ran out of guesses on this question.")
    break

# Statistics etc
print()
print("Game over!")
print(f"You scored {points} points.")
print(f"Thanks for playing, {playerName.title()}!")

# Write the player's name to the scores table we made earlier
print("Your score will be written to an external file. Here are the top 5 scores!")
scorestable.append([playerName.title() + ":", points])
scorestable.sort(reverse=True, key=sortFunc)

# For each element of scores table, write a new line in scores.txt of that score
scores = open("scores.txt", "w")
for i in scorestable:
  scores.write(f"{i[0]} {i[1]}\n")

# Print the top 5 scores (or if there's not 5 scores, just the entire list)
for i in range(0,(len(scorestable) >= 5 and 5 or len(scorestable))):
  print(f"{scorestable[i][0]} {scorestable[i][1]}")

# Close the file to prevent buffers from killing our previous inputs
scores.close()
