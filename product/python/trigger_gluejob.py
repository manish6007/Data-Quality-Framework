import sys
from awsglue.utils import getResolvedOptions
from dq_framework.glue_runner import DQGlueRunner

args = getResolvedOptions(sys.argv, ["CONFIG_PATH", "DATABASE", "RESULTS_BUCKET", "RESULTS_PREFIX"])

runner = DQGlueRunner(
    config_path=args["CONFIG_PATH"],
    database=args["DATABASE"],
    results_bucket=args["RESULTS_BUCKET"],
    results_prefix=args["RESULTS_PREFIX"]
)

runner.run()
