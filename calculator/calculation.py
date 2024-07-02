class Calculation:
    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __repr__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"
