from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import DataFrame


class GlueReader:
    def __init__(self, glue_context: GlueContext, database: str):
        self.glue_context = glue_context
        self.database = database
        self.spark = glue_context.spark_session

    def get_table_data(self, table_name: str) -> DataFrame:
        try:
            df = self.spark.sql(f"SELECT * FROM {self.database}.{table_name}")
            return df
        except Exception as e:
            raise RuntimeError(f"Failed to load table {self.database}.{table_name}: {str(e)}")
