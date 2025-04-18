import json
import boto3
from datetime import datetime
from typing import List


def save_results_to_s3(results: List[dict], bucket: str, prefix: str = "dq-results"):
    """
    Save data quality results to S3 as a JSON file.

    Args:
        results (List[dict]): List of data quality check results.
        bucket (str): S3 bucket name.
        prefix (str): Folder/prefix path within the S3 bucket.
    """
    s3 = boto3.client("s3")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    key = f"{prefix}/dq_results_{timestamp}.json"

    try:
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(results, indent=2).encode("utf-8"),
            ContentType="application/json"
        )
        print(f"[✔] Results uploaded to s3://{bucket}/{key}")
    except Exception as e:
        print(f"[✘] Failed to upload results to S3: {str(e)}")
