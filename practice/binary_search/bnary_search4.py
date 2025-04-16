##Count negative numbers in a sorted matrix
def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1
    for i in range(size):
        mid=(start+end)//2
        if (arr[mid]==target):
              return arr[mid+1]
        elif(arr[mid]>target):
            end=mid-1
        elif(arr[mid]<target):
            start=mid+1
    return arr[0]

my_list=['c', 'f', 'j']
target='a'
result=binary_search(my_list,target)
print(result)