"""
Instructions:
The goal is to build a calculator program.

Storing Functions as a Variable Value
You can store a reference to a function as a value to a variable. e.g.

	def add(n1, n2):
	    return n1 + n2


	my_favourite_calculation = add
	my_favourite_calculation(3, 5)  # Will return 8

In the starting file, you'll see a dictionary that references each of the mathematical calculations that can be performed by our calculator. Try it out and see if you can get it to perform addition, subtraction, multiplication and division.

PAUSE 1
To Do: Write out the other 3 functions - subtract, multiply and divide.

PAUSE 2
To Do: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

PAUSE 3
To Do: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

Functionality
- Program asks the user to type the first number.
- Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
- Program asks the user to type the second number.
- Program works out the result based on the chosen mathematical operator.
- Program asks if the user wants to continue working with the previous result.
 - If yes, program loops to use the previous result as the first number and then repeats the calculation process.
 - If no, program asks the user for the fist number again and wipes all memory of previous calculations.
- Add the logo from art.py
"""
"""
Demo from AppBrewery:
https://appbrewery.github.io/python-day10-demo/
"""

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
