# ml_model.py
from sklearn.linear_model import LinearRegression
import pandas as pd
import logging


def apply_ml_model(data):
    # Example: Apply a simple linear regression model to predict age in 10 years
    model = LinearRegression()
    model.fit(data[['age']], data['age_in_10_years'])

    # Make predictions
    data['predicted_age_in_10_years'] = model.predict(data[['age']])

    logging.info("ML model applied to data.")
    return data