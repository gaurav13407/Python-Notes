##Floyds Triangle
rows=5
num=1
for i in range(0,rows+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
""" 
output:
1
23
456
78910
1112131415
"""