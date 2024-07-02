import pandas as pd

class History:
    def __init__(self):
        self.history = pd.DataFrame(columns=["command", "result"])

    def add_entry(self, command, result):
        new_entry = {"command": command, "result": result}
        self.history = self.history.append(new_entry, ignore_index=True)

    def save_to_csv(self, filename="history.csv"):
        self.history.to_csv(filename, index=False)

    def load_from_csv(self, filename="history.csv"):
        self.history = pd.read_csv(filename)
