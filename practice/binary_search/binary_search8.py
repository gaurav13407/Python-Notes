def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif(arr[mid]>target):
            end=mid-1
        elif(arr[mid]<target):
            start=mid+1
    return -1

print(binary_search([1,2,3,4,5,6],5))
    