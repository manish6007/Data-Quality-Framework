from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class ConsistencyCheck:
    def __init__(self):
        pass

    def run(self, df: DataFrame, config: dict) -> dict:
        """
        Checks logical consistency between columns using defined expressions.

        Args:
            df (DataFrame): Spark DataFrame to check.
            config (dict): Contains 'rules' with logical expressions to validate.

        Returns:
            dict: Results with pass/fail for each rule.
        """
        rules = config.get("rules", [])
        results = {}

        for idx, rule in enumerate(rules):
            name = rule.get("name", f"rule_{idx+1}")
            expression = rule["expression"]

            try:
                inconsistent_count = df.filter(f"NOT ({expression})").count()
                results[name] = {
                    "expression": expression,
                    "inconsistent_count": inconsistent_count,
                    "status": "PASS" if inconsistent_count == 0 else "FAIL"
                }
            except Exception as e:
                results[name] = {
                    "expression": expression,
                    "error": str(e),
                    "status": "ERROR"
                }

        return {
            "check_type": "consistency",
            "results": results
        }
