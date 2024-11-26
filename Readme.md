# ETL Pipeline with Apache Airflow and BigQuery

This project demonstrates a complex ETL pipeline orchestrated with Apache Airflow. The pipeline extracts data from various sources, performs transformations, applies machine learning models, performs data validation and enrichment, and loads the processed data into Google BigQuery.

## Features
- Data extraction from CSV and incremental loading.
- Data transformation with data preprocessing, machine learning model application, and feature engineering.
- Data quality validation with custom checks.
- Data loading into Google BigQuery.
- Notifications and error handling integrated into the pipeline.

## Setup and Installation

### Prerequisites

- Python 3.9 or higher
- Docker (for containerization)
- Google Cloud account with BigQuery and Cloud Storage access
- Apache Airflow 2.x (for orchestration)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/etl-pipeline-phd.git
   cd etl-pipeline-phd
   
docker build -t etl-pipeline .
docker run -d -p 8080:8080 etl-pipeline