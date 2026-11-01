# Program to read student details and display total & percentage

# Reading student details
name = input("Enter Student Name: ")
usn = input("Enter Student USN: ")

print("Enter marks for three subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))

# Calculating total and percentage
total = m1 + m2 + m3
percentage = (total / 300) * 100

# Displaying details
print("\n--- Student Details ---")
print("Name:", name)
print("USN:", usn)
print("Marks:", m1, m2, m3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
