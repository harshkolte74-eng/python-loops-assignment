# Stage 2: Result Check (Positive/Negative)

# Input
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = 0

# Calculation
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
else:
    print("Invalid Operator")

# Result print karo
print("Result =", result)

# Check karo Positive, Negative ya Zero
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")