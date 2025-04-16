##Maximum difference between two consecutive elements in a list.
def difference(lst):
    if len(lst)<2:
        return 0
    max_diff=abs(lst[1]-lst[0])
    
    for i in range(1,len(lst) -1):
        diff=abs(lst[1+i]-lst[i])
        max_diff=max(max_diff,diff)
        return max_diff
my_list = [1, 3, 10, 7, 2]
print(difference(my_list))
