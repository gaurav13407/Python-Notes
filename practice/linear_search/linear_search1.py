## Program to find the element present in the array or not
def linear_search(arr,target):
    size= len(arr)
    for index in range(0,size):
        if (arr[index]==target):
            return index
    return -1

my_list=[22,34,12,45,66]
target=int(input("enter the target:"))
result=linear_search(my_list,target)
print(result)