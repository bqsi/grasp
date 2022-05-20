# Bubble Sort Algorithm

# Bubble sort is a sorting algorithm that iterates through a list, compares elements side by side and swaps them if they're in the wrong order.

'''
Main elements of this algorithm are as follows:
A base list
Iteration
Comparing 2 elements side by side that are one after another
Swapping them if they're in the wrong order
'''

# First, let's get the base list
# We'll just use a list of numbers 1 - 10 which are scrambled

List = [10,1,3,9,8,5,6,7,4,2]

# Now, since we're gonna iterate until it's done, let's write a variable to decide whether or not it's done
# It will start off as false, since the list isn't sorted yet
Sorted = False

# Now, while it's not sorted, let's perform that iteration
while not Sorted:
  # Sorted items is a variable that we're gonna use to gauge whether the list is sorted or not.
  SortedItems = 0
  for n in range(len(List)-1):
    # Declare the list items we're gonna be comparing.
    Element1 = List[n]
    if n >= len(List)-1:
      continue
    Element2 = List[n+1]

    # What condition are we asking?
    # What's gonna decide whether we'll swap the elements or not?

    # If we refer back to our base requirements..
    # The element will swap if the first one is higher than the second.
    # That way, the list is sorted in an ascending order.
    if Element1 > Element2:
      # Now, how do we perform the action of swapping the two elements around?
      List[n] = Element2
      List[n+1] = Element1
      # The reason this works is because we already have Element1 and Element2 casted. They won't change unless we redefine them.
      # They're not a function, which means reusing them won't redefine them.
    else:
      SortedItems += 1
  # Ask whether SortedItems is equal to the length of the list.
  # That equation will return true or false and that value will be assigned to the variable.
  Sorted = (SortedItems == len(List)-1)

  print(List)
  
