"""

Hiya! 👋

This is naughts and crosses featuring a player and a hard coded AI.
The AI makes decisions based on the state of the board - it is not a developing system.

I took inspiration from another 'Tic Tac Toe' Python program that I saw, but NONE of the code is spliced or directly taken.

The code is commented heavily and probably includes some of my thoughts when I was writing the code.
GLHF!

"""

# -- Libraries & Initial Vars -- #
import random

# The board is 9 strings which will either be ' ', 'X' or 'O'.
# I did want them to be numbers at first (0 = Empty, 1 = Naught, 2 = Cross) 
# but it just made it annoying to print the board. 
# Strings are also easier to read and sometimes easier
# to work with.

# The board is declared later, so we'll just cast it now but not really give it a conclusive value.
board = []

# Games list.
games = []

# Playing state.
playing = True

# Initiation / introduction.
print("Welcome to Naughts and Crosses!")
print("This game will be played against an AI. Only one player is required.")
print("Press enter to start at any time.")
input()

# -- Functions -- #

# We'll be using these at a lot of points in the games,
# hence me putting them into functions.

# An annoyingly manual way of printing out the board.
# The logic inside prints the number for user experience points if the space isn't already taken.
# It can look a little clustered, but honestly I just like the feel it gives.
def showBoard(board):
  # Just in case..
  if not board:
    raise Exception("An unknown error has occured. Please restart the program.")
  # You get the idea.
  print()
  print(f"{(board[0] == ' ') and ' ' or board[0]}|{(board[1] == ' ') and ' ' or board[1]}|{(board[2] == ' ') and ' ' or board[2]}")
  print('-+-+-')
  print(f"{(board[3] == ' ') and ' ' or board[3]}|{(board[4] == ' ') and ' ' or board[4]}|{(board[5] == ' ') and ' ' or board[5]}")
  print('-+-+-')
  print(f"{(board[6] == ' ') and ' ' or board[6]}|{(board[7] == ' ') and ' ' or board[7]}|{(board[8] == ' ') and ' ' or board[8]}")
  print('-+-+-')
  print()

def duplicateBoard(b):
  # Make a blank table.
  dupe = []

  # Append all elements of the board to the dupe.
  for i in b:
    dupe.append(i)

  # Return the duplicated board.
  return dupe

# Decide the winner based on a very manual bit of logic.
def decideWinner(b, l):
  # board is b to save my fingers.
  # Same goes for l.
  return (b[0] == l and b[1] == l and b[2] == l) or (b[3] == l and b[4] == l and b[5] == l) or (b[6] == l and b[7] == l and b[8] == l) or (b[0] == l and b[3] == l and b[6] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[0] == l and b[4] == l and b[8] == l) or (b[2] == l and b[4] == l and b[6] == l)

# Assign the player their letter.
def assignPlayer():
  inp = ''
  while not (inp.lower() == "x" or inp.lower() == "o"):
    inp = input("Would you like to be X, or O? ")
  # Logic to decide whether the player picked X or O.
  # One is the basic inverse of the other.
  return ("x" in inp.lower() and "X" or "O"), ("o" in inp.lower() and "X" or "O")

# Return whether a space is empty or not.
def isSpaceEmpty(b, n):
  # Really simple:
  # Returns true if board[n] is ' ', false if not.
  return b[n] == ' '

# Is the board full?
# Will iterate through the board's elements and just break to return False
# if they are not ' '.
def isBoardFull(b):
  for i in range(0,8):
    if isSpaceEmpty(b, i):
      return False
  return True

# Move function.
# Provide a board, letter and position.
def makeMove(b, l, pos):
  b[pos] = l

# Pick a random move to do based off of a moveset.
# Workflow:
# If a space from the moveSet provided is empty, add it to possible moves.
# Return a random pos from the possibleMoves so long as a random move is actually possible.
# Otherwise, just return nothing.
# In making this, I found out about random.choice. Very nice function.
def pickRandomMove(b, moveSet):
  possibleMoves = []
  for pos in moveSet:
    if isSpaceEmpty(b, pos):
      possibleMoves.append(pos)

  return (len(possibleMoves) > 0) and random.choice(possibleMoves) or None

# Logic for the computer's move.
# Comments inside.
def getComputerMove(l):
  # Honestly, when I tried to do this with "var = condition and n" it kept messing up.
  # So.. I just went with the manual route.
  # Could literally be pL = l == "X" and "O" or "X", but for some reason Python didn't accept that.
  if l == "X":
    pL = "O"
  else:
    pL = "X"

  # Here's our algorithm for the N&C AI:

  # NOTE: You'll be seeing a dupe board be declared a lot.
  # That's for logic so we don't operate on the real board when
  # the AI is deciding what move to make.

  # First, let's see if we can win in the next move!
  for i in range(len(board)):
    dupe = duplicateBoard(board)
    if isSpaceEmpty(dupe, i):
      makeMove(dupe, l, i)
      if decideWinner(dupe, l):
        return i
  
  # Can the player win on their next move? If so, let's block them!
  for i in range(len(board)):
    dupe = duplicateBoard(board)
    if isSpaceEmpty(dupe, i):
      makeMove(dupe, pL, i)
      if decideWinner(dupe, pL):
        return i

  # If a corner is free, take one of them!
  m = pickRandomMove(board, [0, 2, 6, 8])
  if m != None:
    return m

  # If the centre is free, take that!
  if isSpaceEmpty(board, 4):
    return 4
  
  # If all else fails, just pick one of the sides.
  return pickRandomMove(board, [1, 3, 5, 7])

# Allow a player to input their move and make that move on the board
def getPlayerMove(l):
  move = 0
  while move not in [1,2,3,4,5,6,7,8,9] or not isSpaceEmpty(board, move-1):
    try:
      move = int(input("Pick a space to move on: (0-9) "))
      if not isSpaceEmpty(board, move-1): print("That space is already taken, please try again!")
    except ValueError:
      print("Your input was invalid, please try again!")
    except:
      print("An unknown error has occured, please try again!")
      
  return move - 1

# Play again logic.
# Returns true if they want to, false if not.
def playAgain():
  inp = ''
  while not (inp.lower() == "y" or inp.lower() == "n"):
    inp = input("Would you like to play again? (Y/N) ")
  return (inp.lower() == "y" and True or False)

# Shorthand for a continue prompt.
def continuePrompt():
  print("Press enter to continue.")
  input()

# - Actual playing code from here on out - #

while True:
  board = [' '] * 9
  pL, cL = assignPlayer()
  turn = random.choice(["player", "computer"])
  print(f"The {turn} will go first.")
  playing = True

  while playing:
    if turn == "player":
      continuePrompt()
      print("It's the player's turn.")
      showBoard(board)

      m = getPlayerMove(pL)
      makeMove(board, pL, m)
      turn = "computer"
    else:
      print("It's the computer's turn.")

      m = getComputerMove(cL)
      makeMove(board, cL, m)
      print(f"The computer picked position {m+1}.")
      showBoard(board)
      turn = "player"
    
    if decideWinner(board, pL):
      showBoard(board)
      print("The player wins!")
      games.append("Player")
      playing = False
    elif decideWinner(board, cL):
      showBoard(board)
      print("The computer wins!")
      games.append("Computer")
      playing = False
    elif isBoardFull(board):
      showBoard(board)
      print("The game is a tie!")
      games.append("Draw")
      playing = False

  if not playAgain():
    break

# End game logic.
# Evaluate all games played, add to counters.
pGames = 0
cGames = 0
dGames = 0
for g in games:
  if g == "Player":
    pGames += 1
  elif g == "Computer":
    cGames += 1
  else:
    dGames += 1

# Print game stats.
print(f"You played {len(games)} game(s).")
print(f"You won {pGames} game(s).")
print(f"You lost {cGames} game(s).")
print(f"You drew {dGames} game(s).")
print()
print("Full games list: ")
for i in range(len(games)):
  print(f"Game {i+1}: {games[i]}")