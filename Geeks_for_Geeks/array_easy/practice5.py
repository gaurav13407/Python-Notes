def second_larger(arr):
    n=len(arr)
    if n<2:
        return -1
    largest=arr[0]
    second_larger=-1
    for i in range(n):
        if arr[i]>largest:
            second_larger=largest
            largest=arr[i]
        elif arr[i]>second_larger and arr[i]!=largest:
            second_larger=arr[i]
            
    return second_larger
    
arr=[2,3,5,1,7,7,4]
ans=second_larger(arr)
print(ans)