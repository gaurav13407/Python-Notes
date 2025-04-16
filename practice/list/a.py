## basics of list in python
## This is how we print the list
a=[1,2,3,4,5,6,7]
print(a)## output:[1, 2, 3, 4, 5, 6, 7]
## print the specific element in list with the help of index
print(a[1])## output:2
## we can also print the element after the specific index
print(a[2:])##output:[3, 4, 5, 6, 7]
## we also print it in reverse after the specfic index
print(a[:6])## output:[1, 2, 3, 4, 5, 6]
## we can also print the list with escaping the elements with the help of steps
print(a[::2])## output:[1, 3, 5, 7]
## There are two Methods to reverse the list
## 1st one:
print(a[::-1])## output:[7, 6, 5, 4, 3, 2, 1]
## 2nd one is with the help of the function:
a.reverse()
print(a)## output:[7, 6, 5, 4, 3, 2, 1]
## How to add the something in the list:
a=[1,2,3,4,5,6,7]
a.append(8)
print(a)##output:[1, 2, 3, 4, 5, 6, 7, 8]
## we can also add somrthing in the desried location on the list
a.insert(1,"apple")
print(a)## output:[1, 'apple', 2, 3, 4, 5, 6, 7, 8]
## we can also modified the list:
a[3]="gaurav"
print(a) ##output:[1, 'apple', 2, 'gaurav', 4, 5, 6, 7, 8]
## we can also remove something from the lsit;
a.remove("apple")
print(a)## output:[1, 2, 'gaurav', 4, 5, 6, 7, 8]
## we can also remove and return the last element of the list
popped_a=a.pop()
print(a.pop)## output:8
print(a)## output:[1, 2, 'gaurav', 4, 5, 6, 7]
## we can also check the index of any element present in the list:
index=a.index("gaurav")
print(index)## output:2
## we can also count if there is any duplicate element present in the list
a=[1,2,3,3,5,6,3,5]
print(a.count(3))## output:3 times 3 present
## we can also sort the list in ascending order
a=['s','a','d','e','t']
a.sort()
print(a)## output:['a', 'd', 'e', 's', 't']
## we can also clear the list by using a function;
a.clear()
print(a)## output:[] empty list
## we can also slic the list as we desired
a=[1,2,3,4,5,6,7]
print(a[1:5])## output:[2, 3, 4, 5]
## we can also iterate over a list with the help of the loop
for a in a:
    print(a)
    ## output:1
2
3
4
5
6
7

## WE can also comprehension the list
lst=[]
for i in range(10):
    lst.append(i**2)
print(lst)## output:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
## basic list comprehension
square=[i**2 for i in range(10)]
print(square)## output:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
##List Comparension with condition
lst=[]
for i in range(10):
    if i%2==0:
        lst.append(i)
print(lst)## output:[0, 2, 4, 6, 8]
## another method:
lst=[num for num in range(10) if num%2==0]
print(lst)## output:[0, 2, 4, 6, 8]
## Nested list Comphrension:
lst1=[1,2,3,4]
lst2=['a','b','c','d']
pair=[(i,j)for i in lst1 for j in lst2]
print(pair)## output:[(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd')]
## list comprehension with function calls:
word=["gaurav","hello","aditya","ram"]
length=[len(word)for word in word]
print(length)##[6, 5, 6, 3]