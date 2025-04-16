## find element present or not in a sorted list
def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            start=mid+1
        elif(arr[mid]>target):
            end=mid-1
    return -1

sorted_list=[12,23,33,47,56,62]
target=int(input("enter the target:"))
result=binary_search(sorted_list,target)
print(result)