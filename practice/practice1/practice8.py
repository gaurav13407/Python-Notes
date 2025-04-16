## decimal to binary without using the bin() function.
def decimal(n):
    if n==0:
        return 0
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n=n//2
    return binary
    
decimal_number=10
binary_number=decimal(decimal_number)
print(binary_number)