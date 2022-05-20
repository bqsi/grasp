# Initial Variables #

# Since we can iterate through strings using keys, we can just put the alphabet into one whole string
# A space is at the end of the alphabet to make encoding a bit more fun
alphabet = "abcdefghijklmnopqrstuvwxyz "

# Encode / Decode Functions #

# These functions are pretty much the same, so only encoding will be commented
def encodemessage(msg, n):
  # To eliminate the risk of cases clashing, etc, conv msg to its lower form.
  msg = msg.lower()

  # Make a temporary alphabet table and also a temporary table for the original message.
  msglist = []
  tempalph = []

  # Append the alphabet to a table.
  for x in alphabet:
    tempalph.append(x)

  # Append the message to a table.
  for x in msg:
    msglist.append(x)

  # To make sure we have the index without having to spam .index methods, use a 'for _ in range(_)'' loop so that we can hold onto the index.
  for x in range(len(msglist)):
    # Collect the individual letter in the message.
    char = msglist[x]

    # Add the given number as n onto the index of wherever the character is in the alphabet.
    i = tempalph.index(char) + n

    # If its over the limit of the alphabet,
    # Have i subtracted from the length of tempalph to fix this.
    if i > len(tempalph):
      i = i - len(tempalph)

    # Make the character in the original message the new index, as decided above.
    msglist[x] = tempalph[i]

    # Make the new message the joined version of msglist.
    msg = ''.join(msglist)
  # Return the message.
  return msg

# Please read lines 10 - 45 for the encode/decode comments.
# This is encode message, just reversed, basically.
def decodemessage(msg, n):
  msg = msg.lower()
  msglist = []
  tempalph = []

  for x in alphabet:
    tempalph.append(x)

  for x in msg:
    msglist.append(x)

  for x in range(len(msglist)):
    char = msglist[x]

    i = tempalph.index(char) - n

    if i > len(tempalph):
      i = i + len(tempalph)

    msglist[x] = tempalph[i]

    msg = ''.join(msglist)
  return msg

# Menu Code #

print("Welcome to the shift encoder.")
print("Please pick an option from the menu when it appears.")

# Basic menu code.
# Standard while true with range checks for each input, yada yada.
# You get it.
while True:
  print("1) Make a code\n2) Decode a message\n3) Quit\n")

  inp = 0

  while not inp in [1,2,3]:
    inp = int(input())
  
  if inp == 1:
    text = input("Please enter a message: ")
    
    valid = False
    n = 0
    while not valid:
      n = int(input("Please enter a number between 1 and 26: "))

      if not n in range(27):
        valid = False
        print("Invalid input!")
      else:
        valid = True
    print(encodemessage(text, n))
  elif inp == 2:
    text = input("Please enter a message: ")
    
    valid = False
    n = 0
    while not valid:
      n = int(input("Please enter a number between 1 and 26"))

      if not n in range(27):
        valid = False
        print("Invalid input!")
      else:
        valid = True
    print(decodemessage(text, n))
  else:
    break

print("Thank you for using the shift encoder.")
