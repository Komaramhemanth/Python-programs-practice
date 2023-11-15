# Function to print a stars pattern
def print_stars_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows for the stars pattern: "))

# Call the function to print the stars pattern
print_stars_pattern(num_rows)
