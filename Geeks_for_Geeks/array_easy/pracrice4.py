## Better approach for finding the second largest

def second_largest(arr):
    n=len(arr)
    if n==1 and n==0:
        return -1
    
    larger=max(arr)
    second_large=-1
    
    for i in range(n):
        if arr[i]>second_large and arr[i]!=larger:
            second_large=arr[i]
    return second_large
    
   

arr=[2,3,5,1,7,7,4]
ans=second_largest(arr)
print(ans)