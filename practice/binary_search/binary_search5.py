##Find First and Last Position of Element in Sorted Array
def first_binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if (arr[mid]==target):
                  return (mid)
        elif(arr[mid]>target):
            end=mid-1
        elif(arr[mid]<target):
            start=mid+1
    return -1

def last_binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if (arr[mid]==target):
                  return mid+1
        elif(arr[mid]>target):
            start=mid+1
        elif(arr[mid]<target):
            start=mid+1
        else:
            end=mid-1
            
    return -1

my_list=[5, 7, 7, 8, 8, 10]
target=5
result1=first_binary_search(my_list,target)
result2=last_binary_search(my_list,target)
print(result1,result2)