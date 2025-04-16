def second_largest(arr):
    n=len(arr)
    if n==0 and n==1:
        print(-1,-1)
    arr.sort()
    small=arr[1]
    large=arr[n-2]
    return small,large

arr=[4,2,5,6,8,1]
ans=second_largest(arr)
print(ans)

## Another brute approach

def second_largest1(arr):
    n=len(arr)
    if n==1 and n==0:
        return (-1,-1)
    
    larger=int()
    second_large=int()
    
    
    larger=max(arr)
    arr.sort()
    for i in range(n-2,0,-1):
        if arr[i]!=larger:
          second_large=arr[i]
          break
        
    return second_large

arr=[2,3,5,1,7,7,4]
ans=second_largest1(arr)
print(ans)