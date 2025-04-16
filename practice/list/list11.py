##Check if all elements in a list are Unique
def unique(lst):
    return len(lst)==len(set(lst))
lst=[1,2,3,4,5]
print(unique(lst))## output:True
lst=[1,2,3,4,2,4]
print(unique(lst))## output:False
