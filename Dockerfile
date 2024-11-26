# Use an official Apache Airflow image as a base
FROM apache/airflow:2.6.2-python3.9

# Set the working directory
WORKDIR /opt/airflow

# Install necessary Python dependencies
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the DAGs and scripts into the container
COPY dags/ /opt/airflow/dags/
COPY scripts/ /opt/airflow/scripts/
COPY config/ /opt/airflow/config/

# Set up logging and configurations
COPY config/logging_config.py /opt/airflow/config/logging_config.py
COPY config/airflow_config.py /opt/airflow/config/airflow_config.py

# Expose the Airflow web server port
EXPOSE 8080

# Start Airflow webserver and scheduler
CMD ["bash", "-c", "airflow db init && airflow scheduler & airflow webserver"]