# Advanced Calculator

## Overview

An advanced Python-based calculator application designed for IS218. This project demonstrates the importance of professional software development practices, including clean and maintainable code, design patterns, comprehensive logging, dynamic configuration, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Features

- Basic arithmetic operations (Add, Subtract, Multiply, Divide)
- Calculation history management with Pandas
- Comprehensive logging
- Dynamic configuration via environment variables
- Extensible plugin system
- Command-Line Interface (REPL)

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/tishamadhok/advanced_calculator.git
   cd advanced_calculator
2. **Create and Activate Virtual ENviornment** 
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**
    pip install -r requirements.txt
4. **Set Up Environment Variables**
    LOG_LEVEL=DEBUG
    LOG_FILE=app.log

## Usage

1. **Running the REPL**
    python -m calculator.repl
    **You will see a prompt like this:**
    Welcome to the advanced calculator REPL. Type 'exit' to quit.
    calc>
2. **Perform Operations**
    Addition: add 1 2
    Subtraction: subtract 5 3
    Multiplication: multiply 3 4
    Division: divide 8 2
    View History: history
    Exit: exit

5. **Design Patterns:**
    Facade Pattern: Simplifies the interface for complex Pandas data manipulations.
    Command Pattern: Structures commands within the REPL for effective calculation and history management.
    Factory Method, Singleton, and Strategy Patterns: Enhance the application's code structure, flexibility, and scalability.

6. **Logging:**
    The application uses Python's logging module to record detailed application operations, data manipulations, errors, and informational messages. The logging configuration is dynamically adjustable via environment variables.

7. **Testing:**
   Run Test:
   pytest -v --cov=calculator tests/
   **Ensure test coverage is above 90%**


8. **Contributing:**
    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature/your-feature).
    Create a new Pull Request.

9. **License:**
    MIT License 

10. **Acknowledgments:**
    Pandas
    Python-dotenv
    Pytest

