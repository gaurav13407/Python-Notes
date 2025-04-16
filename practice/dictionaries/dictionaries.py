## Dictionaries In python
##Dictionaries are unordered collection of items. They store data in key-values pairs.
# Keys must be unique and immutable (e.g.strings,number,or tuples),while value can be of any type.
## How to create a dicitionaries
students={"name":"gaurav","age":32,"grade":24}
print(students)## output:{'name': 'gaurav', 'age': 32, 'grade': 24}
## How to access the dicitionaries
print(students['name'])## output:gaurav
print(students['age'])## output:32
## What happend when i call something that are not present in the list
##print(students['last_name'])## an error has come
##print(students['last_name',"Not avilable"])## with this we can overcome the error
## How to modifiy the dictionaries
students['age']=22
print(students)## output:{'name': 'gaurav', 'age': 22, 'grade': 24}
## How to add new key and value
students['addres']="india"
print(students)## output:{'name': 'gaurav', 'age': 22, 'grade': 24, 'addres': 'india'}
## HOw to delete the key
del students['grade']
print(students)## output:{'name': 'gaurav', 'age': 22, 'addres': 'india'}
## dictionaries methods
keys=students.keys()
print(keys)##output:dict_keys(['name', 'age', 'addres'])
values=students.values()
print(values)##output:dict_values(['gaurav', 22, 'india'])
##Shallow copy
students_copy=students
print(students)##output:{'name': 'gaurav', 'age': 22, 'addres': 'india'}
print(students_copy)##output:{'name': 'gaurav', 'age': 22, 'addres': 'india'}
## The same output has printed as expected but now when i made a change in student dictionaries the change has been also made in students_copy dictionaries.
students['name']="krish"
print(students)## output:{'name': 'krish', 'age': 22, 'addres': 'india'}
print(students_copy)##output:{'name': 'krish', 'age': 22, 'addres': 'india'}
## The output has been made in both the dictionaries even though we only modified students.and to over come this we use .copy() function.
students_copy1=students.copy()
students['name']="guarav"
print(students)## output:{'name': 'guarav', 'age': 22, 'addres': 'india'}
print(students_copy1)## output:{'name': 'krish', 'age': 22, 'addres': 'india'}
## Iteration over dictinories:
## you can use loop to iterate over dictionaries,keys,value or items
 ## Iterating over the keys
for keys in students.keys():
     print(keys)## output:name age addres
## I can do the same for the values:
for value in students.values():
    print(value)## output:guarav  22   india
    
## Iterate over key value pair
for key,value in students.items():
    print(f"{key}:{value}")## output:name:guarav age:22 addres:india

## Nested dictionaries
students={
    "student1":{"name":"gaurav","age":32},
    "student2":{"name":"peter","age":35}   
}
print(students)## output:{'student1': {'name': 'gaurav', 'age': 32}, 'student2': {'name': 'peter', 'age': 35}}
## how to acces nested dictionaries elements
print(students['student1']['name'])## output:gaurav
print(students['student2']['name'])## output:peter
## I can also see the all items in the dictionaries by .items() function
items=students.items() 
print(items)## output:dict_items([('student1', {'name': 'gaurav', 'age': 32}), ('student2', {'name': 'peter', 'age': 35})])
## Iterating over the nested dictionaries
for students_id,students_info in students.items():
    print(f"{students_id}:{students_info}")
    for keys,value in students_info.items():
        print(f"{key}:{value}")
## output:
"""student1:{'name': 'gaurav', 'age': 32}
addres:gaurav
addres:32
student2:{'name': 'peter', 'age': 35}
addres:peter
addres:35"""
## Dictionaries comphrension
square={x:x**2 for x in range(5)}
print(square)## output:{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
## conditional dictionary comprehension
square={x:x**2 for x in range(10) if x%2==0}
print(square)## output:{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

