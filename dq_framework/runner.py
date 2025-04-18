from dq_framework.checks import CHECK_TYPE_MAP
from pyspark.sql import DataFrame


def run_quality_checks(df: DataFrame, table_config: dict) -> list:
    """
    Run all configured checks on the provided DataFrame.

    Args:
        df (DataFrame): Spark DataFrame to run checks on.
        table_config (dict): Dictionary containing checks for one table.

    Returns:
        list: A list of results from each check.
    """
    results = []
    table_name = table_config.get("table")
    for check_type, check_config in table_config.items():
        if check_type == "table":
            continue
        if check_type not in CHECK_TYPE_MAP:
            results.append({
                "check_type": check_type,
                "status": "SKIPPED",
                "reason": "Unknown check type"
            })
            continue

        checker = CHECK_TYPE_MAP[check_type]()
        result = checker.run(df, check_config)
        result["table"] = table_name
        results.append(result)

    return results
