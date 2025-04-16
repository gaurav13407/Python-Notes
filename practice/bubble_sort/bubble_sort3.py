def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr

Sorted_list=bubble_sort([2,4,1,8,6,7,9])
print(Sorted_list)