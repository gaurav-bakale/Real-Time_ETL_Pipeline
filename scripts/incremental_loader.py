# incremental_loader.py
import pandas as pd
from google.cloud import storage
import logging


def load_incremental_data(last_run_timestamp):
    """
    Incrementally load new or modified data based on the last run timestamp.
    """
    # Load the full dataset (for simplicity, we're using a CSV file as a mock source)
    data = pd.read_csv('full_data.csv')  # Mock data source (replace with real DB/API)

    # Filter data based on timestamp to only get new rows
    new_data = data[data['timestamp'] > last_run_timestamp]

    # Upload the filtered data to GCS
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('your-gcs-bucket-name')
    blob = bucket.blob('data/incremental_data.csv')
    new_data.to_csv(blob.open('w'), index=False)

    logging.info(f"Incremental data loaded and uploaded to GCS: {len(new_data)} rows.")
    return new_data