from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, when


class CompletenessCheck:
    def __init__(self):
        pass

    def run(self, df: DataFrame, config: dict) -> dict:
        """
        Check for null values in specified columns.

        Args:
            df (DataFrame): Spark DataFrame to be checked.
            config (dict): Config containing columns to check.

        Returns:
            dict: Summary of null counts per column.
        """
        results = {}
        columns = config.get("columns", [])

        for column in columns:
            null_count = df.select(count(when(col(column).isNull(), column)).alias("nulls")).collect()[0]["nulls"]
            results[column] = {
                "null_count": null_count,
                "status": "PASS" if null_count == 0 else "FAIL"
            }

        return {
            "check_type": "completeness",
            "results": results
        }
