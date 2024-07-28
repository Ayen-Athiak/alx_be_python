class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Prints the class attribute `calculation_type` before performing the multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Usage of Calculator class methods
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")  # Output: The sum is: 15

    # Using the class method
    product_result = Calculator.multiply(4, 3)
    print(f"The product is: {product_result}")  # Output: The product is: 12
