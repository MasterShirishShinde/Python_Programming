import math

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, x, y):
        result = x + y
        self.history.append(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            result = "Error! Division by zero."
        else:
            result = x / y
        self.history.append(f"{x} / {y} = {result}")
        return result

    def exponent(self, x, y):
        result = x ** y
        self.history.append(f"{x} ^ {y} = {result}")
        return result

    def square_root(self, x):
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result

    def modulo(self, x, y):
        result = x % y
        self.history.append(f"{x} % {y} = {result}")
        return result

    def show_history(self):
        if not self.history:
            print("No calculations yet.")
        else:
            print("Calculation History:")
            for entry in self.history:
                print(entry)

    def clear_history(self):
        self.history.clear()
        print("History cleared.")

def run_calculator():
    calc = Calculator()

    operations = {
        '1': ("Add", calc.add),
        '2': ("Subtract", calc.subtract),
        '3': ("Multiply", calc.multiply),
        '4': ("Divide", calc.divide),
        '5': ("Exponent (x^y)", calc.exponent),
        '6': ("Square Root", calc.square_root),
        '7': ("Modulo", calc.modulo),
        '8': ("Show History", calc.show_history),
        '9': ("Clear History", calc.clear_history)
    }

    while True:
        print("\nSimple Calculator - Choose an operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1-9) or '0' to quit: ")

        if choice == '0':
            print("Thanks for using the Calculator!")
            break
        elif choice not in operations:
            print("Invalid option, please choose a valid number.")
            continue

        if choice == '8':
            calc.show_history()
            continue
        elif choice == '9':
            calc.clear_history()
            continue

        try:
            if choice == '6':  
                num = float(input("Enter number: "))
                result = operations[choice][1](num)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = operations[choice][1](num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Error! Please enter valid numeric values.")

run_calculator()
