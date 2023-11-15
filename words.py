def print_unique_words(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the contents of the file
            content = file.read()

            # Split the content into words and convert them to lowercase
            words = [word.lower() for word in content.split()]

            # Get unique words and sort them alphabetically
            unique_words = sorted(set(words))

            # Print the unique words
            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user for the file path
    file_path = input("Enter the path of the text file: ")
    print_unique_words(file_path)

