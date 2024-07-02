import importlib
import os

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        plugins_dir = os.path.dirname(__file__)
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                plugin_name = filename[:-3]
                module = importlib.import_module(f"calculator.plugins.{plugin_name}")
                self.plugins[plugin_name] = module

    def get_plugins(self):
        return self.plugins
