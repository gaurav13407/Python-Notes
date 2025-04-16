##: Valid Perfect Square
import math

def is_perfect_square(num):
    if num < 0:
        return False  # Negative numbers cannot be perfect squares
    sqrt = math.isqrt(num)  # This returns the integer square root
    return sqrt * sqrt == num

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is a perfect square
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")