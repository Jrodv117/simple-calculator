def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


calculator_dictionary = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

num1 = int(input("First number:"))
num2 = int(input("Second number:"))

for key in calculator_dictionary:
    print(key)

operation_symbol = input("Pick an operation listed above: ")


calculation = calculator_dictionary[operation_symbol]

answer = calculation(num1, num2)
