def rotate_array(arr):
    n=len(arr)
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=arr[i]
    temp[n-1]=arr[0]
    for i in range(n):
        print(temp[i],end=",")
    print()
    

arr=[1,2,3,4,5]
ans=rotate_array(arr)
print(ans)