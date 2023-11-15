# fibonacci_module.py

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
# main_program.py

# Importing the custom Fibonacci module
import fibonacci_module

# Taking user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Using the function from the imported module to generate Fibonacci numbers
fibonacci_sequence = fibonacci_module.generate_fibonacci(n)

# Displaying the generated Fibonacci sequence
print(f"Fibonacci Sequence of {n} numbers: {fibonacci_sequence}")
