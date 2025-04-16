## program to interchange first and last elements in a list
lst=[1,2,3,4,5,6]
print(lst)## output[1, 2, 3, 4, 5, 6]
## Interchange the first and last element in the list
lst[0],lst[-1]=lst[-1],lst[0]
##Now the element has changed.
print(lst)## output:[6, 2, 3, 4, 5, 1]