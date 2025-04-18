# 🛠️ AWS Data Quality Framework

A scalable, configurable, and team-friendly Data Quality Framework built for AWS Glue and PySpark. This framework helps you validate your data on S3 or Glue Catalog tables using rules defined in a simple YAML or JSON format.

---

## 🚀 Features

- ✅ Rule-based data quality checks
- 📦 Distributable as a Python package
- 📁 Config-driven (YAML or JSON)
- 🔥 Scales via AWS Glue and Spark
- ☁️ Results saved to S3
- 💬 Easily pluggable for teams

---

## 📁 Project Structure

```
aws-dq-framework/
├── dq_framework/                  # Included in .whl
│   ├── config_loader.py
│   ├── glue_reader.py
│   ├── runner.py
│   ├── utils.py
│   ├── glue_runner.py            # Class that runs DQ logic
│   └── checks/
│       ├── completeness.py
│       ├── accuracy.py
│       ├── consistency.py
│       ├── timeliness.py
│       └── uniqueness.py
├── examples/
│   └── config.yaml               # Sample rule configuration
├── setup.py                      # Packaging definition
└── README.md
```

---

## 🔧 Data Quality Checks

Each check is defined in a config file. Supported types:

- `completeness`: Null checks
- `accuracy`: Value range or allowed values
- `consistency`: Cross-field logic
- `timeliness`: Freshness check (date columns)
- `uniqueness`: Duplicate row detection

---

## 📜 Example Config

```yaml
checks:
  - table: customers
    completeness:
      columns: ["customer_id", "email"]

  - table: customers
    accuracy:
      rules:
        status:
          allowed_values: ["active", "inactive"]
        age:
          min: 18
          max: 100

  - table: customers
    consistency:
      rules:
        - name: age_and_signup
          expression: age > 0 AND signup_date IS NOT NULL

  - table: orders
    timeliness:
      columns: ["order_date"]
      threshold_days: 30

  - table: customers
    uniqueness:
      columns: ["customer_id"]
```

---

## 🚀 Run with AWS Glue

You can run this framework as a Glue job with:

```bash
--CONFIG_PATH=s3://your-bucket/config.yaml
--DATABASE=your_glue_database
--RESULTS_BUCKET=your-results-bucket
--RESULTS_PREFIX=dq-results
```

---

## 💾 Save Results

All DQ results are saved to S3 as timestamped JSON files:

```json
[
  {
    "check_type": "completeness",
    "results": {
      "email": {
        "null_count": 0,
        "status": "PASS"
      }
    },
    "table": "customers"
  }
]
```

---

## 🧱 Install as a Package

To install locally:

```bash
pip install -e .
```

---

## 📦 Build and Distribute as .whl

To package the framework for use with AWS Glue or to upload to a private Nexus repository:

1. Ensure you have the latest `setuptools` and `wheel` installed:
   ```bash
   pip install --upgrade setuptools wheel
   ```

2. Navigate to the root of the project:
   ```bash
   cd aws-dq-framework
   ```

3. Run the following to build the `.whl` file:
   ```bash
   python setup.py bdist_wheel
   ```

4. The output will be placed in the `dist/` folder:
   ```bash
   dist/aws_dq_framework-0.1.0-py3-none-any.whl
   ```

5. Upload this file to your private Nexus repository or copy it to S3.

---

## 📄 License

MIT License

---

## 🧠 Author

Built with ❤️ by Manish Shrivastava
