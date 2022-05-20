# Introductory Parts
import random
print("Welcome to Rock Paper Scissors!")
print("One user is required to play this game.")
print("The computer will generate a random number and that will be interpreted as rock, paper or scissors.")
print("You can stop the game at any time by giving 'end' to any input prompts and your game history will be printed after the ongoing match is finished.")

input("Press enter at any time to start.\n")

# Define variables for use later on

ended = False
list = []

# Define generate input and take input functions
# geninput() will serve the CPU, takeinput() will serve the user

def geninput():
  # Essentially: Generate a random number between 1 and 3 and decide R, P or S from that number
    n = random.randint(1, 3)
    return n == 1 and "rock" or n == 2 and "scissors" or "paper"

def takeinput():
  # Essentially:
  # - Take input "R, P or S?"
  # - Interpret response (or wait for a correct response in a loop)
  # - Decide R, P, S or 'end' based on said response
  # - Return said response
    rps = ""
    validinput = False
    while not validinput:
        try:
            rps = input("Rock, Paper or Scissors? ")
        except:
            print("An error has occurred. Please try again!")
        else:
            ended = "end" in rps.lower() and True or False
            validinput = "rock" in rps.lower() or "paper" in rps.lower() or "scissors" in rps.lower() or ended and True or False
            if not validinput:
                print("Invalid input. Please try again!")
    return rps

# While a game is running...
while ended == False:
    print(f"Game {len(list) + 1}.")
    if input("Press enter to continue.\n").lower() == "end": break

    print("It's the user's turn.")
    user1 = takeinput()
    if user1.lower() == "end": break
    print(f"You chose {user1}.\n")
    print("It's the computer's turn.")
    user2 = geninput()
    print(f"The computer chose {user2}.")
    
    # RPS Logic based on actual game rules
    # - Decides winner
    # - Casts winner for each round to 'winner'
    # - 'winner' is used later
    if user1.lower() == user2.lower():
        print("Draw!\n")
        winner = "Draw"
    elif "rock" in user1.lower():
        if "paper" in user2.lower():
            print("Computer wins!\n")
            winner = "Computer"
        else:
            print("User 1 wins!\n")
            winner = "User"
    elif "paper" in user1.lower():
        if "scissors" in user2.lower():
            print("Computer wins!\n")
            winner = "Computer"
        else:
            print("User 1 wins!\n")
            winner = "User"
    elif "scissors" in user1.lower():
        if "rock" in user2.lower():
            print("Computer wins!\n")
            winner = "Computer"
        else:
            print("User 1 wins!\n")
            winner = "User"
    # Append the winner of this round to 'list'. More on that later.
    list.append(winner)

# Define user and cpu wins as well as draws for later
userwins = 0
cpuwins = 0
draws = 0

# Essentially:
# - Iterate through list and give it a value for each time someone won a game [1]
for i in list:
    if "User" in i: userwins += 1
    if "Computer" in i: cpuwins += 1
    if "Draw" in i: draws += 1

# Print game statistics. Break lines are messy, but just easier.
print(f"You played {len(list)} games.\n")
print(f"You won {userwins} game(s).\nThe CPU won {cpuwins} game(s).\nYou had {draws} draw(s).")
print("Below is a full list of logged games.\n")


# [1]
# Essentially:
"""
  I use a for i in range loop here to make sure that "i" remains as the current index.
  
  Each value in 'list' now comes into play!
  For each value in 'list', print the game's number (determined by the index + 1***)
  + the winner, which was determined by the value in 'list' in that specific index.

  ***Python indexes start at 0, not 1. We'll add 1 to reflect the actual number!***
"""
for i in range(len(list)):
    print(f"Game {i + 1}: {list[i]}")
