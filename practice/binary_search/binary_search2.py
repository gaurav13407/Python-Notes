def binary_function(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        elif(arr[mid]<target):
            start=mid+1
    return -1

sorted_list=[13,21,36,49,52,67]
target=21
result=binary_function(sorted_list,target)
print(result)