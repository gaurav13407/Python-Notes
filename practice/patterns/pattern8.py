##Right Angled Triangle
def tringle(n):
    for i in range(0,n+1):
        for j in range(i):
            print('*',end="")
        print()
        
print(tringle(5))
##output:
""" 
*
**
***
****
*****
"""