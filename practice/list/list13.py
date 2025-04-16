## Count Number of Odd and Even Elements in a List
numbers=[1,2,3,4,5,6,7,8]
count_even=[]
count_odd=[]
for number in numbers:
    if number%2==0:
        count_even.append(number)
    else:
        count_odd.append(number)

print("even number are:",count_even)##output:[2, 4, 6, 8]
print("odd number are:",count_odd)##output:[1, 3, 5, 7]