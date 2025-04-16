def rotated_Array(arr,k):
    n=len(arr)
    if k>0:
        k=k%n
        return arr[-k:]+arr[:-k]
    else:
        return arr[k:]+arr[:k]
    
ans=rotated_Array([1,2,3,4,5],1)
print(ans)