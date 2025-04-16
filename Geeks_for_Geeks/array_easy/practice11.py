def remove_dulpicate(arr):
    i=0
    n=len(arr)
    for j in range(1,n):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 4]
    k = remove_dulpicate(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")