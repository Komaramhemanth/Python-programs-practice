def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# User input for temperature in Celsius
celsius_temperature = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_result = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is equal to {fahrenheit_result} Fahrenheit")

# User input for temperature in Fahrenheit
fahrenheit_temperature = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius_result = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenheit is equal to {celsius_result} Celsius")
