def safe_divide (numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        results = f"The result of the division is {numerator/denominator}"
        return results
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError:
        return f"Error: Please enter numeric values only."

