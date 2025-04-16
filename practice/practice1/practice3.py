'''def prime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
        else :
            return True
    
n=int(input("enter the number:"))
result=prime(n)
print(result)'''
# Get input from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')

