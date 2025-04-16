def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if(arr[i]==target):
            return i
    return -1
my_list=[12,53,34,36,62]
target=36
result=linear_search(my_list,target)
print(result)