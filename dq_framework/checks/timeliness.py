from pyspark.sql import DataFrame
from pyspark.sql.functions import col, current_date, datediff


class TimelinessCheck:
    def __init__(self):
        pass

    def run(self, df: DataFrame, config: dict) -> dict:
        """
        Validates that date columns are recent within a given threshold.

        Args:
            df (DataFrame): Spark DataFrame to validate.
            config (dict): Dict with 'columns' and max allowed age in days.

        Returns:
            dict: Timeliness check result for each date column.
        """
        results = {}
        threshold_days = config.get("threshold_days", 30)
        columns = config.get("columns", [])

        for column in columns:
            try:
                outdated_count = df.filter(datediff(current_date(), col(column)) > threshold_days).count()
                results[column] = {
                    "outdated_count": outdated_count,
                    "threshold_days": threshold_days,
                    "status": "PASS" if outdated_count == 0 else "FAIL"
                }
            except Exception as e:
                results[column] = {
                    "error": str(e),
                    "status": "ERROR"
                }

        return {
            "check_type": "timeliness",
            "results": results
        }
