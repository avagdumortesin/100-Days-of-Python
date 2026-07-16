import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def math_operation(previous_result):
    if previous_result is None:
        n1 = float(input("Enter the first number: "))
    else:
        n1 = previous_result
    operation = input("Pick an operation:\n+\n-\n*\n/\n")
    n2 = float(input("Enter the second number: "))
    new_result = arithmetic_functions[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {new_result}")
    return new_result

arithmetic_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

result = None

while True:
    result = math_operation(result)
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if again == "n":
        result = None
