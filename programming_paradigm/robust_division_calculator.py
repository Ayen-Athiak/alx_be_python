def safe_divide (numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        results = numerator/denominator
        return results
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")

    except ValueError:
        print(f"Error: Please enter numeric values only.")

