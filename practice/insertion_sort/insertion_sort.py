def insertion_sort(arr):
    n=len(arr)
    for current in range(1,n):
        currentcard=arr[current]
        correctposition=current-1#It will go from i-1 to 0
        
        while(correctposition>=0):
            if(arr[correctposition]<currentcard):
                break
            else:
                arr[correctposition+1]=arr[correctposition]
                correctposition-=1
                
            arr[correctposition+1]=currentcard
    return arr


unsorted_list=[12,25,11,34,90,22]
sorted_list= insertion_sort(unsorted_list)
print("sorted elements:",sorted_list)