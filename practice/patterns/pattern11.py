##Pyramid Pattern
def pyramid(rows):
    for i in range(1,rows+1):
        ##printing the spaces
        print(" "*(rows-i),end="")
        ## printing the stars
        print("*"*(2*i-1))
        
rows=5
print(pyramid(rows))
""" 
output:
   *
   ***
  *****
 *******
*********
"""