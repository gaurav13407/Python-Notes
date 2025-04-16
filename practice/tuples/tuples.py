## Introduction to tuples
##Tuples are ordered collection of items that are immutable.They are similar to lists,but their immutability makes them different.
## How tp create a tuple
numbers=tuple()
print(type(numbers))## outptut:<class 'tuple'>
numbers=tuple([1,2,3,4,5,6])
print(numbers)## output:(1, 2, 3, 4, 5, 6)
## mixed tuples
mixed_tuples=(1,"hello",3.14,True)
print(mixed_tuples)## output:(1, 'hello', 3.14, True)
## Aceesing number in tuple
print(numbers[2])##output:3
print(numbers[-1])##output:6
## we can also slice it up
print(numbers[0:4])## output:(1, 2, 3, 4)
## I can also reverse it 
print(numbers[::-1])## output:(6, 5, 4, 3, 2, 1)
## Tuples concatenation
concatenation=numbers+mixed_tuples
print(concatenation)## output:(1, 2, 3, 4, 5, 6, 1, 'hello', 3.14, True)
## We can also multiply the tuples and print it multiple time
print(mixed_tuples*3) ## output:(1, 'hello', 3.14, True, 1, 'hello', 3.14, True, 1, 'hello', 3.14, True)
##Immutable nature of tuples
## we cannot modified tuple its shows us error
## Tuple Methods
print(numbers.count(1))##output:1
print(numbers.index(3))##output:2
## packing and unpacking of tuple
packed_tuple=1,"hello",3.14,True
print(packed_tuple) ## output:(1, 'hello', 3.14, True)
## unpacking the tuple
"""a,b,c = packed_tuple
print(a)
print(b)
print(c)"""
##Unpacking with*
numbers=(1,2,3,4,5,6)
first,*middle,last=numbers
print(first)#output:1
print(middle)##output:[2, 3, 4, 5]
print(last)## output:6
## Nested tuple
## Nested list
lst=[[1,2,3,4],[6,7,8,9],[1,"hello",3.14,"c"]]
lst[0][0:3]
lst=[[1,2,3,4],[6,7,8,9],(1,"hello",3.14,"c")]
lst[2][0:3]
nested_tuple=((1,2,3,4),("a","b","c"),(True,False))
## access The Elements inside a tuple
print(nested_tuple[0])
print(nested_tuple[1][2])
