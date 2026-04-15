# Stage 1: Basic Calculator

# User se input lo
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Calculation logic
if op == '+':
    result = num1 + num2
    print("Result =", result)

elif op == '-':
    result = num1 - num2
    print("Result =", result)

elif op == '*':
    result = num1 * num2
    print("Result =", result)

elif op == '/':
    # Division by zero check
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result =", result)

else:
    print("Invalid Operator")