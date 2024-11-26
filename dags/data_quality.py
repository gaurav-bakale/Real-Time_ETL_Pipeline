# data_quality.py
import pandas as pd
import logging


def data_quality_checks(data):
    # Check for null values
    if data.isnull().any().any():
        raise ValueError("Data contains null values!")

    # Check for data type consistency (e.g., age should be a numeric column)
    if not pd.api.types.is_numeric_dtype(data['age']):
        raise ValueError("Age column has incorrect data type!")

    logging.info("Data quality checks passed.")