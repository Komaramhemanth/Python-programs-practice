# Create a tuple
my_tuple = (1, 2, 3, 'apple', 'banana')

# Access elements in a tuple
print("Tuple elements:")
for element in my_tuple:
    print(element)

# Access a specific element
print("\nThird element of the tuple:", my_tuple[2])

# Concatenate tuples
tuple1 = (4, 5, 6)
tuple2 = ('orange', 'grape')
combined_tuple = my_tuple + tuple1 + tuple2
print("\nCombined Tuple:", combined_tuple)

# Tuple unpacking
a, b, c, *rest = combined_tuple
print("\nUnpacked variables:")
print("a =", a)
print("b =", b)
print("c =", c)
print("Rest of the tuple:", rest)
