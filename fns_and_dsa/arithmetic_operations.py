def perform_operation(num1, num2, operation):
    print("Arithmetic Operations")
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Your number is indivisible"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

# Example usage


results = perform_operation(3, 0, "divide")

print(f"Results: {results}")


