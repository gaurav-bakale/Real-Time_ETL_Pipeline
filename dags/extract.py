# extract.py
import pandas as pd
from google.cloud import storage
import logging


def extract_data(last_run_timestamp):
    # Simulate extraction from a CSV or API (for demonstration)
    logging.info(f"Extracting data since last run: {last_run_timestamp}")

    data = pd.read_csv('data_source.csv')  # Example CSV
    new_data = data[data['timestamp'] > last_run_timestamp]  # Incremental extraction logic

    # Save extracted data to Google Cloud Storage
    storage_client = storage.Client()
    bucket_name = 'your-gcs-bucket-name'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob('data/incremental_data.csv')
    new_data.to_csv(blob.open('w'), index=False)

    logging.info("Incremental data extracted and uploaded to GCS.")
    return new_data