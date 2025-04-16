## We can also use binary search to find if the element present in the array or not but there is one condition and is that the array must have been sorted.
def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid##found the target
        elif (arr[mid]>target):
            end=mid-1
        elif(arr[mid]<target):
            start=mid+1
    return -1

sorted_list=[10,20,30,40,50,60]
target=30
result=binary_search(sorted_list,target)
print(result)
 