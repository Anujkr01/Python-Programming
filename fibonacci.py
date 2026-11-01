N=int(input("Enter the length of fibonacci sequence:"))
a,b = 0,1
print("fibonacci sequence:")
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b