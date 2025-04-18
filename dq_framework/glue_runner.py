import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

from dq_framework import ConfigLoader, GlueReader
from dq_framework.runner import run_quality_checks
from dq_framework.utils import save_results_to_s3


class DQGlueRunner:
    def __init__(self, config_path: str, database: str, results_bucket: str, results_prefix: str):
        self.config_path = config_path
        self.database = database
        self.results_bucket = results_bucket
        self.results_prefix = results_prefix

        self.sc = SparkContext()
        self.glue_context = GlueContext(self.sc)

        self.config = ConfigLoader(self.config_path).get_checks()
        self.reader = GlueReader(self.glue_context, self.database)

    def run(self):
        all_results = []
        for check_conf in self.config:
            table_name = check_conf["table"]
            df = self.reader.get_table_data(table_name)
            results = run_quality_checks(df, check_conf)
            all_results.extend(results)

        save_results_to_s3(all_results, bucket=self.results_bucket, prefix=self.results_prefix)
        print("[✔] Data quality checks completed and results saved.")
