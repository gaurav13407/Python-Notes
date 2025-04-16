def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
unsroted_array=[23,12,45,35,64]
sorted_array=bubble_sort(unsroted_array)
print(sorted_array)
##output:[12, 23, 35, 45, 64]