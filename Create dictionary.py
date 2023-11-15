# Create a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Access values in a dictionary
print("Dictionary values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Access a specific value
print("\nAge:", my_dict['age'])

# Modify a value
my_dict['age'] = 26
print("\nUpdated Age:", my_dict['age'])

# Add a new key-value pair
my_dict['occupation'] = 'Engineer'
print("\nUpdated Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Remove a key-value pair
removed_key = 'city'
if removed_key in my_dict:
    del my_dict[removed_key]
    print(f"\nDictionary after removing '{removed_key}': {my_dict}")
else:
    print(f"'{removed_key}' not found in the dictionary.")

# Check if a key is present
search_key = 'name'
if search_key in my_dict:
    print(f"\n'{search_key}' found in the dictionary. Value: {my_dict[search_key]}")
else:
    print(f"\n'{search_key}' not found in the dictionary.")
