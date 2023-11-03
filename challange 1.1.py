def factorial(n):
    # Base case: If n is 0 or 1, the factorial is 1.
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: Factorial of n is n multiplied by factorial of (n-1).
        return n * factorial(n - 1)

# Test the function
number = 5  # You can change this to any non-negative integer
result = factorial(number)
print(f"The factorial of {number} is {result}")
