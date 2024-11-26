# load.py
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
import logging


def load_data_to_bigquery():
    # Define BigQuery destination table and source path in GCS
    dataset_id = 'your-bigquery-dataset-id'
    table_id = 'your-bigquery-table-id'
    gcs_path = 'data/transformed_data.csv'

    # Load data from GCS to BigQuery
    load_task = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket='your-gcs-bucket-name',
        source_objects=[gcs_path],
        destination_project_dataset_table=f"{dataset_id}.{table_id}",
        source_format='CSV',
        skip_leading_rows=1,
        autodetect=True,
        write_disposition='WRITE_APPEND',
    )
    load_task.execute(context={})

    logging.info(f"Data loaded into BigQuery table {dataset_id}.{table_id}.")