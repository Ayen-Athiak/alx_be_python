def perform_operation(num1,num2,operation):
    num1 =float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    if num2 == 0:
            print("this number cannot be divide")
    else:return num1 / num2
result= perform_operation("num1","num2","operation")
print(f"results:{result}")



