# data_validation.py
import pandas as pd
import logging


def validate_data(data):
    """
    Validate the integrity of the data: Check for missing values, duplicates, and outliers.
    """
    # Check for missing values
    if data.isnull().sum().any():
        raise ValueError("Data contains missing values.")

    # Check for duplicate rows
    if data.duplicated().any():
        raise ValueError("Data contains duplicate rows.")

    # Check for outliers (assuming 'age' is a numerical column for this example)
    age_mean = data['age'].mean()
    age_std = data['age'].std()
    age_outliers = data[(data['age'] < (age_mean - 3 * age_std)) | (data['age'] > (age_mean + 3 * age_std))]

    if not age_outliers.empty:
        logging.warning(f"Detected outliers in 'age': {age_outliers}")

    logging.info("Data validation passed.")
    return data