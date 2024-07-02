import sys
from calculator.core import Calculator
from calculator.history import History
from calculator.logging_config import logger

def repl():
    calc = Calculator()
    history = History()
    while True:
        try:
            command = input("calc> ").strip().split()
            if not command:
                continue
            if command[0] in ['exit', 'quit']:
                break
            if command[0] == 'history':
                print(history.df)
                continue
            if len(command) != 3:
                print("Invalid command. Usage: <operation> <a> <b>")
                continue
            op, a, b = command[0], float(command[1]), float(command[2])
            result = None
            if op == 'add':
                result = calc.add(a, b)
            elif op == 'subtract':
                result = calc.subtract(a, b)
            elif op == 'multiply':
                result = calc.multiply(a, b)
            elif op == 'divide':
                result = calc.divide(a, b)
            else:
                print(f"Unknown operation: {op}")
                continue
            history.add_record(op, a, b, result)
            print(f"Result: {result}")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error: {e}")

if __name__ == '__main__':
    repl()
