def findlargest(arr):
    n=len(arr)
    max_number=arr[0]
    for i in range(0,n):
        if max_number<arr[i]:
           max_number=arr[i]
    return max_number

arr=[2,1,4,8,3,6,2]
ans=findlargest(arr)
print(ans)