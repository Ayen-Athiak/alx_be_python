def perform_operation(Num1, Num2,Operation):
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation =="add":
        return num1 + num2
    elif operation == "subtract" :
        return num1 - num2
    elif operation =="multiply":
        return num1 * num2
    elif operation=="divide" and num2 == 0:
        return "you number is indivisible"
    else:return num1 /num2





results = perform_operation('num1','num2','operation')


print(f"results:{results}")


