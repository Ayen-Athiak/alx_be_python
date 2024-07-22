def safe_divide (numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        results = f"The result of the division is {numerator/denominator}"
        return results
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")

    except ValueError:
        print(f"Error: Please enter numeric values only.")

