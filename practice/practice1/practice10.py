##binary to decimal without using int() function
def decimal_number(binary):
    decimal=0
    binary=binary[::-1]
    for i in range(len(binary)):
        if binary[i]=='1':
            decimal+=2**i
    return decimal

binary_number="1010"
result=decimal_number(binary_number)
print(result)