# Stage 3: Student Grade Calculator

# Input lo
name = input("Enter Student Name: ")
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

# Total aur Percentage
total = m1 + m2 + m3
percentage = (total / 300) * 100

# Grade check karo
grade = ""

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Final Output
print("Name:", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)