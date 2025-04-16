def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if (arr[j]<arr[min_index]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

unsorted_list=[23,4,32,12,53,64]
sorted_list=selection_sort(unsorted_list)
print(sorted_list)##[4, 12, 23, 32, 53, 64]