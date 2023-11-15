# Function to check if the triangle is a right triangle
def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()

    # Check the Pythagorean Theorem
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Get user input for the lengths of the sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("It's a right triangle!")
else:
    print("It's not a right triangle.")
