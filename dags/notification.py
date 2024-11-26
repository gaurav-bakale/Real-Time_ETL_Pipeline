# notifications.py
from airflow.hooks.base_hook import BaseHook
from airflow.operators.email_operator import EmailOperator
from airflow.exceptions import AirflowException

def send_failure_alert(dag_id, task_id):
    subject = f"Airflow Task Failed: {dag_id} - {task_id}"
    html_content = f"The following task in DAG {dag_id} failed: {task_id}. Please check logs for more details."

    email = EmailOperator(
        task_id='send_email',
        to=['your_email@example.com'],
        subject=subject,
        html_content=html_content,
    )
    email.execute(context={})

    raise AirflowException(f"Task {task_id} failed in DAG {dag_id}")