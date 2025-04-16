def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


unsorted_list=[23,1,34,64,74,31]
sorted_list=bubble_sort(unsorted_list)
print(sorted_list)##output:[1, 23, 31, 34, 64, 74]