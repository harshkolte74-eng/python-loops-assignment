# Stage 1: Basic Calculator

# Taking input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = 0

# Logic using if-elif-else
if operator == '+':
    result = num1 + num2
    print(f"Result = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result = {result}")
elif operator == '/':
    # Handling division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"Result = {result}")
else:
    print("Invalid operator")