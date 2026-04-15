# Stage 2: Calculator with Result Check

# Taking input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = 0
is_valid = True # Flag to check if calculation happened

# Logic using if-elif-else
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        is_valid = False
    else:
        result = num1 / num2
else:
    print("Invalid operator")
    is_valid = False


# Display result and check Positive/Negative/Zero

if is_valid:
    print(f"Result = {result}")
    
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")