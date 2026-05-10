# Calculate and print the factorial of n (5! = 5 × 4 × 3 × 2 × 1).

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
