# Function to perform arithmetic operations
def perform_arithmetic_operations(a, b):
    # Addition
    sum_result = a + b
    print(f"Sum: {a} + {b} = {sum_result}")

    # Subtraction
    difference_result = a - b
    print(f"Difference: {a} - {b} = {difference_result}")

    # Multiplication
    product_result = a * b
    print(f"Product: {a} * {b} = {product_result}")

    # Division
    if b != 0:
        division_result = a / b
        print(f"Division: {a} / {b} = {division_result}")
    else:
        print("Cannot divide by zero.")

    # Modulus
    if b != 0:
        modulus_result = a % b
        print(f"Modulus: {a} % {b} = {modulus_result}")
    else:
        print("Cannot calculate modulus with zero divisor.")

    # Exponentiation
    exponentiation_result = a ** b
    print(f"Exponentiation: {a} ** {b} = {exponentiation_result}")

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
perform_arithmetic_operations(num1, num2)
