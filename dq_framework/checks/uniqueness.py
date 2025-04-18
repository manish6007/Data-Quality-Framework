from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count as spark_count


class UniquenessCheck:
    def __init__(self):
        pass

    def run(self, df: DataFrame, config: dict) -> dict:
        """
        Checks for duplicate rows based on one or more key columns.

        Args:
            df (DataFrame): Spark DataFrame to validate.
            config (dict): Dict with 'columns' to validate uniqueness.

        Returns:
            dict: Result showing duplicate count and pass/fail status.
        """
        columns = config.get("columns", [])
        if not columns:
            return {
                "check_type": "uniqueness",
                "error": "No columns provided for uniqueness check.",
                "status": "ERROR"
            }

        try:
            duplicate_count = (
                df.groupBy(columns)
                  .agg(spark_count("*").alias("count"))
                  .filter(col("count") > 1)
                  .count()
            )

            return {
                "check_type": "uniqueness",
                "columns": columns,
                "duplicate_count": duplicate_count,
                "status": "PASS" if duplicate_count == 0 else "FAIL"
            }
        except Exception as e:
            return {
                "check_type": "uniqueness",
                "columns": columns,
                "error": str(e),
                "status": "ERROR"
            }
