## Linear search 

def linear_search(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    else:
        return -1
    
    
print(linear_search([1,4,2,4,5,3],4))
    