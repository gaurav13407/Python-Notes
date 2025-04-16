##Decimal to Binary
##The bin() function returns the binary representation of a decimal number as a string, prefixed with "0b".
decimal_number=int(input("enter the number:"))
binary_number=bin(decimal_number)[2:]## with the help of this we can avoid the first 2 digit of 0b present when using bin() function.
print(binary_number)