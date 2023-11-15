class PowerCalculator:
    def pow(self, x, n):
        # Base case: x^0 is always 1
        if n == 0:
            return 1

        # If n is negative, calculate the reciprocal of x^n
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            # Square x and reduce n by half
            x *= x
            n //= 2

        return result

if __name__ == "__main__":
    # Example usage
    power_calculator = PowerCalculator()
    
    # Example 1: 2^3
    result1 = power_calculator.pow(2, 3)
    print(f"2^3 = {result1}")

    # Example 2: 3^-2
    result2 = power_calculator.pow(3, -2)
    print(f"3^-2 = {result2}")
2^3 = 8
3^-2 = 0.1111111111111111
