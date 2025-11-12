# This program performs basic arithmetic operations using match-case.

# Step 1: Get user inputs & operation (without decimals)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

# Step 2: Use match case to perform the operation
match operation:
    case "+":
        result = num1 + num2
        print("The result is", result)
    case "-":
        result = num1 - num2
        print("The result is", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("The result is", result)
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
