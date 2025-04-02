import math_tools

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
operation = operation = input("Choose an operation (add, subtract, multiply, divide): ")

if operation == "add":
    result = math_tools.add(a, b)
elif operation == "subtract":
    result = math_tools.subtract(a, b)
elif operation == "multiply":
    result = math_tools.multiply(a, b)
elif operation == "divide":
    result = math_tools.divide(a, b)

print(result)
