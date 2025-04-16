## create a rectangle
def rectangle(n,m):
    for i in range(n):
        
        for j in range(m):
            print('*',end="")
        print()

print(rectangle(4,5))
           
""" output:
*****
*****
*****
*****
"""