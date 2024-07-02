class Calculator:
    def process_command(self, command):
        # Parse and execute command
        # Example for basic operations
        if command.startswith("add"):
            _, x, y = command.split()
            return float(x) + float(y)
        elif command.startswith("subtract"):
            _, x, y = command.split()
            return float(x) - float(y)
        elif command.startswith("multiply"):
            _, x, y = command.split()
            return float(x) * float(y)
        elif command.startswith("divide"):
            _, x, y = command.split()
            return float(x) / float(y)
        else:
            raise ValueError("Unknown command")
