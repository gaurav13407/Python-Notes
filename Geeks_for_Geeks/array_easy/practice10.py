def check_array(arr):
    n=len(arr)
    check_break=0
    for i in range(n):
        if arr[i]>arr[i+1%n]:
            check_break+=1
        
            
        
        if check_break==1:
            return False
    return True