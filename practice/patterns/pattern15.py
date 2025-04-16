##Diamond Pattern
# Number of rows (height of the diamond's half)
rows = 5

# Upper half of the diamond
for i in range(1, rows + 1):
    # Printing spaces
    for j in range(rows - i):
        print(" ", end="")
    # Printing stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # Move to the next line

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    # Printing spaces
    for j in range(rows - i):
        print(" ", end="")
    # Printing stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()  # Move to the next line

""" 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""