def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
                
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

unsorted_list=[23,1,3,24,53,45]
sorted_list=selection_sort(unsorted_list)
print(sorted_list)##output:[1, 3, 23, 24, 45, 53]                