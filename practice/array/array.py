## There are no in build array present we need to import the array to use.In python list is present rather than array.
import array

arr=array.array('i',[1,2,3,4,5])
print(arr)##output:array('i', [1, 2, 3, 4, 5])
## We can also easily acces the element inside the array just like list.
print(arr[0])##output:1
## We can also modifie the array just like list
arr[0]=10
print(arr)##output:array('i', [10, 2, 3, 4, 5])