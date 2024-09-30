
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Get user input
number = int(input("Enter a number: "))

# Check if the input is valid (non-negative)
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and display the result
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")

