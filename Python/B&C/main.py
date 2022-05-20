# - Libraries and Initiation - #
import random

guesses = 0
randnum = []
guess = []

# Rules
print("Welcome to bulls and cows!")
print()
print("The game will run once.")
print("The computer will pick a random 4 digit number with no duplicate digits.")
print()
print("You will try and guess the 4 digit number.")
print("Your guess can not contain duplicate digits.")
print("If your guess has a number which is in the same position in the computer's number, that will be classed as a 'bull'.")
print("If your guess has a number which is in the computer's number but not in the same position, that will be classed as a 'cow'.")
print()
print("You have infinite guesses and the program will exit when you guess the correct number.")
print("You can exit at any time by typing 'exit' into any input field.")
print("Press enter to start the game.")
input()

# - Game code & Functions - #

# Generate a random 4 digit number using the following rules:
# Each digit must be 0-9
# No duplicates
# Cast these nums to a table for use later on
# (We're using a table to help with positioning for comparison)
def generateNum(num):
  for i in range(4):
    random.seed()
    n = str(random.randint(0,9))

    while n in num:
      random.seed()
      n = str(random.randint(0,9))
  
    num.append(n)
  return num

# Input validation function that returns 3 variables:
# A state (whether the input is valid and if so correct or incorrect)
# as well as the bulls and cows numbers for later use.
# Please see the logic inside, I'm too tired to comment it rn
def validateInput(inp, rnum):
  state = ''

  inpj, rnumj = ''.join(inp), ''.join(rnum)

  if inpj == rnumj:
    state = "correct"
  else:
    state = "incorrect"

  b = 0
  c = 0
  for i in inp:
    if inp.count(i) > 1: state = "duplicate"
    if i in rnum:
      if rnum.index(i) == inp.index(i):
        b += 1
      else:
        c += 1
  return state, b, c


# Call 'generateNum' to fill in randnum.
randnum = generateNum(randnum)

# Workflow:
# Initiate guess as a blank table
# While it doesn't consist of 4 items:
# Take an input as a string, just in case they exit
# Make a blank table and append all items of guess to that table
# Make guess that table for comparison later
# Initiate bulls and cows numbers
# Make a joined version of guess and randnum for comparison
# If they're correct, let them know
# If they're not, decide the cows and bulls

while True:
  print()
  guess = []
  while not len(guess) == 4:
    guess = input("Enter a 4 digit number: ")
    if guess == "exit": break
    gd = []
    for i in guess: gd.append(i)
    guess = gd
    if len(guess) < 4: print("\nYou must enter a 4 digit number!")

  state, bulls, cows = validateInput(guess, randnum)

  if state == "correct":
    print("Correct!")
    break
  elif state == "incorrect":
    print("Incorrect.")
    print(f"Your guess had {bulls} bull(s) and {cows} cow(s).")
  else:
    print("You cannot have duplicates in your number!")

print(f"The random number was {''.join(randnum)}")