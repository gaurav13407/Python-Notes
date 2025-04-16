## sort the array using the bubble sort method
def bubble_sort(arr):
    n=(len(arr))
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr  

unsorted_list=[34,12,45,24,6]
sorted_list=bubble_sort(unsorted_list)
print(sorted_list)
## output:[6, 12, 24, 34, 45]
