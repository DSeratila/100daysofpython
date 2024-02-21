import subprocess


def clear():
    subprocess.call("clear")


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("Enter the first number\n"))
    continue_calculating = "y"

    while continue_calculating == "y":
        num2 = float(input("Enter the second number\n"))
        print("Choose operation:")
        for symbol in operations:
            print(symbol)

        symbol = input()

        user_function = operations[symbol]
        result = user_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")

        continue_calculating = input("Wanna continue? y/n\n")

        if continue_calculating == "y":
            num1 = result
        else:
            clear()
            calculator()


calculator()

