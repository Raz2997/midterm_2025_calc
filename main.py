from calculator.calculator import Calculator
import sys

def main():
    try:
        a, b, operation = sys.argv[1], sys.argv[2], sys.argv[3]
        a, b = float(a), float(b)

        operations = {
            "add": Calculator.add,
            "subtract": Calculator.subtract,
            "multiply": Calculator.multiply,
            "divide": Calculator.divide
        }

        if operation not in operations:
            print(f"Unknown operation: {operation}")
            return

        result = operations[operation](a, b)
        print(f"The result of {a} {operation} {b} is equal to {result}")

    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except ValueError:
        print(f"Invalid number input: {sys.argv[1]} or {sys.argv[2]} is not a valid number.")
    except IndexError:
        print("Usage: python main.py <number1> <number2> <operation>")

if __name__ == "__main__":
    main()
