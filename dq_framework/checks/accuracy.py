from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class AccuracyCheck:
    def __init__(self):
        pass

    def run(self, df: DataFrame, config: dict) -> dict:
        """
        Validates column values against given rules (like range, list, regex).

        Args:
            df (DataFrame): Spark DataFrame to validate.
            config (dict): Accuracy check config with rules per column.

        Returns:
            dict: Accuracy check results per column.
        """
        results = {}
        rules = config.get("rules", {})

        for column, rule in rules.items():
            if "allowed_values" in rule:
                allowed = rule["allowed_values"]
                invalid_count = df.filter(~col(column).isin(allowed)).count()
            elif "min" in rule and "max" in rule:
                invalid_count = df.filter((col(column) < rule["min"]) | (col(column) > rule["max"])).count()
            else:
                continue

            results[column] = {
                "invalid_count": invalid_count,
                "status": "PASS" if invalid_count == 0 else "FAIL"
            }

        return {
            "check_type": "accuracy",
            "results": results
        }
