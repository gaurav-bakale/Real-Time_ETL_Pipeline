# data_enrichment.py
import pandas as pd
import logging


def enrich_data(data):
    """
    Enrich the data with additional information from external sources.
    For this example, we'll add random data for demonstration purposes.
    """
    # Mock external data (e.g., demographic data)
    additional_data = pd.DataFrame({
        'region': ['North', 'South', 'East', 'West'],
        'average_income': [55000, 45000, 60000, 70000],
    })

    # Simulate merging the external data with the current dataset
    data['region'] = pd.Series(['North', 'South', 'East', 'West'] * (len(data) // 4))
    data['average_income'] = pd.Series([55000, 45000, 60000, 70000] * (len(data) // 4))

    logging.info("Data enriched with external demographic information.")
    return data