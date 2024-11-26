# transform.py
import pandas as pd
from google.cloud import storage
import logging
from ml_model import apply_ml_model


def transform_data():
    # Load data from GCS
    storage_client = storage.Client()
    bucket_name = 'your-gcs-bucket-name'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob('data/incremental_data.csv')
    data = pd.read_csv(blob.open('r'))

    # Apply transformations and ML model
    transformed_data = apply_ml_model(data)

    # Save transformed data back to GCS
    transformed_blob = bucket.blob('data/transformed_data.csv')
    transformed_data.to_csv(transformed_blob.open('w'), index=False)

    logging.info("Data transformed and uploaded to GCS.")
    return transformed_data