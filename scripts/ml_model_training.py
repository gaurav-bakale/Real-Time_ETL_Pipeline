# ml_model_training.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import logging
import joblib


def train_ml_model(data):
    """
    Train a linear regression model on the data (predicting 'age_in_10_years' based on 'age').
    """
    # Define features and target
    X = data[['age']]
    y = data['age_in_10_years']

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model (simple R-squared value for demonstration)
    r2_score = model.score(X_test, y_test)
    logging.info(f"Model trained with R^2 score: {r2_score}")

    # Save the model to disk (for future use during predictions)
    joblib.dump(model, 'ml_model.pkl')
    logging.info("Model saved as 'ml_model.pkl'")

    return model