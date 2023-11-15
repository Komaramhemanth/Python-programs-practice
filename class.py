class IntegerToRoman:
    def __init__(self):
        # Define the mapping of Roman numerals
        self.roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, num):
        if not (0 < num < 4000):
            raise ValueError("Input must be between 1 and 3999")

        result = ""
        for value, symbol in sorted(self.roman_numerals.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value

        return result

if __name__ == "__main__":
    # Example usage
    integer_to_roman_converter = IntegerToRoman()
    try:
        number = int(input("Enter an integer (1 to 3999): "))
        roman_numeral = integer_to_roman_converter.convert_to_roman(number)
        print(f"The Roman numeral for {number} is: {roman_numeral}")
    except ValueError as ve:
        print(ve)
