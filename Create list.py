# Create a list
my_list = [1, 2, 3, 4, 5]
print("Initial List:", my_list)

# Append elements to the list
my_list.append(6)
my_list.append(7)
print("List after Appending:", my_list)

# Remove elements from the list
element_to_remove = 3
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"List after Removing {element_to_remove}:", my_list)
else:
    print(f"{element_to_remove} not found in the list.")

# Create a second list
another_list = [8, 9, 10]

# Concatenate lists
combined_list = my_list + another_list
print("Combined List:", combined_list)
