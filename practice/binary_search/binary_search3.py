def binary_search(arr,target):
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


my_list=[10,20,30,40,50]
target=40
result=binary_search(my_list,target)
print(result)
