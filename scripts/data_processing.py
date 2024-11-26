# data_preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import logging


def preprocess_data(data):
    """
    Preprocess the data by cleaning missing values, standardizing numerical features, and encoding categorical ones.
    """
    # Handle missing values
    data = data.fillna(data.mean())  # For simplicity, filling with mean for numerical columns

    # Standardize numerical features
    numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    scaler = StandardScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

    # Encoding categorical variables (simple one-hot encoding for this example)
    categorical_columns = data.select_dtypes(include=[object]).columns.tolist()
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    logging.info("Data preprocessing complete.")
    return data