##Sum of N Even Natural Numbers
def sum_of_even_numbers(N):
    # Using the formula: N * (N + 1)
    return N * (N + 1)

# Input from the user
N = int(input("Enter a positive integer N: "))

# Calculate and print the sum of first N even natural numbers
print("The sum of first", N, "even natural numbers is:", sum_of_even_numbers(N))