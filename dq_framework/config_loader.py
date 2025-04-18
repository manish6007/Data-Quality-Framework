import yaml
import json
import os


class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, "r") as file:
            if self.config_path.endswith(".yaml") or self.config_path.endswith(".yml"):
                return yaml.safe_load(file)
            elif self.config_path.endswith(".json"):
                return json.load(file)
            else:
                raise ValueError("Unsupported config file format. Use YAML or JSON.")

    def get_checks(self):
        if "checks" not in self.config:
            raise ValueError("No 'checks' section found in configuration.")
        return self.config["checks"]
