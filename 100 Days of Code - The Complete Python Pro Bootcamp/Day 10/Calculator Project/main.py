import art
print(art.logo)

#TODO: Write out the other 3 functions - subtract, multiply and divide.

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
math_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(number):
    print(" + \n - \n * \n / \n")
    operation = input("Pick an operation: ")
    number2 = float(input("What is the next number?: "))
    result = math_dictionary[operation](number, number2)
    print(f"{number} {operation} {number2} = {result}")
    keep_going = input(f"Type y to continue calculating with {result} or type n to start a new calculation: ")
    return keep_going

number = float(input("What's the first number?: "))
calculator(number)
if calculator(number) == "y":
    calculator(calculator(number))
else:
    number = float(input("What's the first number?: "))
    calculator(number)

