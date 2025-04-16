## Check if the array is sorted brute force approach

def check_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in  range(i+1,n):
            if arr[j]<arr[i]:
                return False
    return True
        
arr=[1,2,3,4,5,6]
ans=check_sort(arr)
print(ans) 