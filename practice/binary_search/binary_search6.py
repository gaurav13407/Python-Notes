##Minimum in Rotated Sorted Array
def first_binary_search(arr):
    size=len(arr)
    for i in range(size-1):
        min=arr[i]
        if(arr[i]<arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return min



list=[4, 5, 6, 7, 0, 1, 2] 
result=first_binary_search(list)
print(result)