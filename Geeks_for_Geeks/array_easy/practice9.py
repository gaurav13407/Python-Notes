## To check if array is sorted and rotated

def rotated_sorted(arr):
    n=len(arr)
    count_breake=0
    for i in range(n):
        if arr[i]>arr[i+1]:
            count_breake+=1
            
        if count_breake==1 and arr[-1]<arr[0]:
            return True
    return False

print(rotated_sorted([4, 5, 6, 1, 2, 3]))