def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid# found the target
        elif(arr[mid]>target):
            start=mid+1
        elif(arr[mid]<target):
            start=mid+1
        
    return -1

list=[4, 5, 6, 7, 0, 1, 2]
target=0
reuslt=binary_search(list,target)
print(reuslt)