"""
print this pattern
* 
* *
* * *
* * * *
* * * * *
"""
r=5
for i in range(r+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()