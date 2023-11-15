class StringReverser:
    def reverse_words(self, input_string):
        # Split the string into words
        words = input_string.split()

        # Reverse the order of the words
        reversed_words = words[::-1]

        # Join the reversed words to form the final reversed string
        reversed_string = ' '.join(reversed_words)

        return reversed_string

if __name__ == "__main__":
    # Example usage
    string_reverser = StringReverser()

    # Example: "Hello World" reversed word by word
    input_string = "Hello World"
    reversed_result = string_reverser.reverse_words(input_string)

    print(f"Original String: {input_string}")
    print(f"Reversed String: {reversed_result}")
