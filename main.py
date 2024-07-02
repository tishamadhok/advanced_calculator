import logging
import os
from calculator.core import Calculator
from calculator.history import History

# Logging configuration
log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
log_file = os.getenv('LOG_FILE', 'app.log')

logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def main():
    calc = Calculator()
    history = History()

    while True:
        try:
            command = input("Enter command: ")
            if command.lower() in ["exit", "quit"]:
                break
            # Process command here
            result = calc.process_command(command)
            history.add_entry(command, result)
            print(f"Result: {result}")
        except Exception as e:
            logging.error("An error occurred", exc_info=True)

if __name__ == "__main__":
    main()
