##Inverted Pyramid Pattern
def inverted_pyramid(rows):
    for i in range(rows,0,-1):
        ##printing spaces
        print(" "*(rows-i),end="")
        ##printing stars
        print("*"*(2*i-1))
        
rows=5
result=inverted_pyramid(rows)
print(result)
""" 
 output:
 *********
 *******
  *****
   ***
    *
 """