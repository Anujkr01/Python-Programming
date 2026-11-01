# Program to generate Fibonacci sequence of length N

# Read N from the console
N = int(input("Enter the length of Fibonacci sequence: "))

a, b = 0, 1

print("Fibonacci Sequence:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
