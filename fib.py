# program to generate fibonacci sequence of lenght N

# Rerad N from the console
N=int(input("Enter the lenght of fibonacci sequence:"))
a, b = 0, 1
print("fibonacci sequence:")
for i in range(N):
    print(a, end= " ")
    a, b = b, a + b