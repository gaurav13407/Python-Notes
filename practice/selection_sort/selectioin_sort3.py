def selectioin_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

sorted_list=selectioin_sort([4,3,1,6,8,5])
print(sorted_list)