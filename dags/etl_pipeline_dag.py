from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract_data
from transform import transform_data
from load import load_data_to_bigquery
from data_quality import data_quality_checks
from notifications import send_failure_alert

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 26),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email_on_retry': False,
}

# Define DAG
dag = DAG(
    'real_time_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
)

# Task 1: Extract Data
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    op_args=['{{ prev_execution_date }}'],
    dag=dag,
)

# Task 2: Transform Data
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

# Task 3: Data Quality Check
quality_check_task = PythonOperator(
    task_id='data_quality_checks',
    python_callable=data_quality_checks,
    op_args=['{{ task_instance.xcom_pull(task_ids="transform_data") }}'],
    dag=dag,
)

# Task 4: Load Data to BigQuery
load_task = PythonOperator(
    task_id='load_data_to_bigquery',
    python_callable=load_data_to_bigquery,
    dag=dag,
)

# Task 5: Send alert on failure
failure_alert_task = PythonOperator(
    task_id='send_failure_alert',
    python_callable=send_failure_alert,
    op_args=['{{ task_instance.dag_id }}', '{{ task_instance.task_id }}'],
    trigger_rule='one_failed',
    dag=dag,
)

# Define task dependencies
extract_task >> transform_task >> quality_check_task >> load_task >> failure_alert_task