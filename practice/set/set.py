## Sets
##sets are built in data type in python used to store collection of unique items.
# they are unordered,meaning that the elements do not follow a specific order,and they do not allow duplicate elements.
# Sets are useful for membership tests,eliminating duplicates entries,and performing mathematical 
# set operation like union,intersection,difference and symmetric difference.
## How to create a set
set={1,2,3,4,5,6,7,8}
print(set)## output:{1, 2, 3, 4, 5, 6, 7, 8}
print(type(set))## output:<class 'set'>
## IN set if there is more than one same element it cannot print the duplicate element twice
my_set={1,2,2,3,4,4,5,5,6}
print(my_set)#output:{1, 2, 3, 4, 5, 6}
## Basic Set operation
##adding and removing 
## to add
my_set.add(8)
print(my_set)## output:{1, 2, 3, 4, 5, 6, 8}
## for remove
set={1,2,3,4,5,6,7}
set.remove(2)
print(set)## output:{1, 3, 4, 5, 6, 7}
## And if I try to remove the element that are not present in set it gave me an error
##but there is a function called discard() to counter that error.It just run the program even though there is not the element present that we want to remove.
set.discard(10)
print(set)##  output:{1, 3, 4, 5, 6, 7}
## There is also the method for us to remove the element from the set and return it.
## And it can be done with the help of the pop() function>
remove=set.pop()
print(remove)## output:1
print(set)## output:{3, 4, 5, 6, 7}
## Now to clear the set and make it an empty set and it can be done with the help of the .clear() function
set.clear()
print(set)## output:() empty set
## We can also check if there is an element present in the set or not
set={1,2,3,4,5}
print(3 in set)## True
print(10 in set)## False
## Now we can also do the mathematical operation on the sets known as union and intersection and difference.
## Union of the set
## In union of the set the element of the both set add together and neglet if any element are repiting.
set1={1,2,3,4}
set2={3,4,5,6}
union=set1.union(set2)
print(union)## output:{1, 2, 3, 4, 5, 6}
## Intersection of an set
## IN Intersection of the set only the common element present in the both set are printed
Intersection=set1.intersection(set2)
print(Intersection)## output:{3, 4}
## Now there is an also a function called the intersection_update it can update the value of set 1 .
set1.intersection_update(set2)
print(set1)## Output:{3, 4}
## Now we can also find the difference in the both set:
## IN difference it can only print that are not present in set 2 but present in set 1.
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
difference=set1.difference(set2)
print(difference)## Output:{1, 2, 3}
## Now as above we can also update the value of set1:
set1.difference_update(set2)
print(set1)## OUtput:{1, 2, 3}
## Now there is also an function called symmetric Differnece:it only remove common element present in the set.
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
symmetric=set1.symmetric_difference(set2)
print(symmetric)## Output:{1, 2, 3, 7, 8, 9}
## Now there is a set Method
set1={1,2,3,4,5}
set2={3,4,5}
print(set1.issubset(set2))## False It because all the element that are present in set 1 are not present in set2
print(set1.issuperset(set2))## True It because if there all element that are present in the set2 are present in set 1 it called superset.
#### How to remove the duplicate elements fro the list just convert it into a set
## There is a simple way to do that we can easily remove the duplicate element just by converting list into the set.
lst=[1,2,3,4,5,5,6]
set(lst)## output:{1, 2, 3, 4, 5}
## counting unique word in text
text="IN THIS tutorial we are discussing about sets"
word=text.split()
## convert list of words of set to get unique words
unique_words=set(word)
print(unique_words)
print(len(unique_words))
##output:{'we', 'IN', 'tutorial', 'discussing', 'sets', 'THIS', 'are', 'about'}
## 8