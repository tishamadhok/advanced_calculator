# main.py

from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
environment = os.getenv('ENVIRONMENT')
api_key = os.getenv('API_KEY')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info(f"Running in {environment} mode with API key: {api_key}")

# Command pattern classes
class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method.")

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        logger.info(f"Adding {self.a} + {self.b} = {result}")
        return result

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        logger.info(f"Subtracting {self.a} - {self.b} = {result}")
        return result

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        logger.info(f"Multiplying {self.a} * {self.b} = {result}")
        return result

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            logger.error("Division by zero error")
            return "Error: Division by zero"
        result = self.a / self.b
        logger.info(f"Dividing {self.a} / {self.b} = {result}")
        return result

class Calculator:
    def execute_command(self, command):
        return command.execute()

def main():
    calc = Calculator()
    while True:
        cmd = input("Enter command (add, subtract, multiply, divide) or 'exit': ").strip().lower()
        if cmd == "exit":
            break
        if cmd in {"add", "subtract", "multiply", "divide"}:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if cmd == "add":
                    command = AddCommand(a, b)
                elif cmd == "subtract":
                    command = SubtractCommand(a, b)
                elif cmd == "multiply":
                    command = MultiplyCommand(a, b)
                elif cmd == "divide":
                    command = DivideCommand(a, b)
                result = calc.execute_command(command)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                logger.error("Invalid input: Non-numeric value entered")
        else:
            print("Invalid command. Please enter add, subtract, multiply, or divide.")
            logger.error(f"Invalid command entered: {cmd}")

if __name__ == "__main__":
    main()
