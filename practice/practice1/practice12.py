'''def largest(arr):
    n=len(arr)
    m=arr[0]
    for i in range(n-1):
        if arr[m]<=arr[i]:
            arr[m]=arr[i]
            
    return arr[m]
    '''

arr=[10,50,20,40,10]
ans=max(arr)
print(ans)
minans=min(arr)
print(minans)