# Stage 3: Student Grade Calculator

# Input
name = input("Enter Student Name: ")
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

# Calculate Total
total_marks = mark1 + mark2 + mark3

# Calculate Percentage
percentage = (total_marks / 300) * 100

# Determine Grade
grade = ""

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("\n--- Result ---")
print(name)
print(f"Total: {total_marks}/300")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")