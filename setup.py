from setuptools import setup, find_packages

setup(
    name="aws-dq-framework",
    version="0.1.0",
    description="Modular and configurable Data Quality Framework for AWS Glue using PySpark",
    author="Manish Shrivastava",
    author_email="manishshrivastava@gmail.com",
    packages=find_packages(include=["dq_framework", "dq_framework.*"]),
    include_package_data=True,
    install_requires=[
        "boto3",
        "pyyaml"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
