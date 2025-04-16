def sum_of_even_numbers(N):
    # Initialize sum to 0
    total_sum = 0
    
    # Loop through first N even numbers
    for i in range(1, N + 1):
        even_number = 2 * i  # The i-th even number is 2 * i
        total_sum += even_number  # Add to the sum
    
    return total_sum

# Input from the user
N = int(input("Enter a positive integer N: "))

# Calculate and print the sum of first N even natural numbers
print("The sum of first", N, "even natural numbers is:", sum_of_even_numbers(N))