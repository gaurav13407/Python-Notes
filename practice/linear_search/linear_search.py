## With the help of the linear search we can also find that the element is present in the array or not.
def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if (arr[i]==target):
            return i
    return -1

my_list=[12,22,43,50,65]##In python we can also use list as a array as long list consist of same type of element(int,char,float, etc.)
target=43
result=linear_search(my_list,target)
print(result)##output:2 index