from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv
import json
import random
import logging

# Load environment variables from the .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract(**kwargs):
    logger.info("Starting extract task")
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': ['A', 'B', 'C']
    })
    df_json = df.to_json(orient='split')
    kwargs['ti'].xcom_push(key='data', value=df_json)
    logger.info(f"Extracted DataFrame: {df}")

def transform(**kwargs):
    logger.info("Starting transform task")
    df_json = kwargs['ti'].xcom_pull(key='data', task_ids='extract')
    df = pd.read_json(df_json, orient='split')
    df['random_number'] = [random.randint(1, 100) for _ in range(len(df))]
    df_json = df.to_json(orient='split')
    kwargs['ti'].xcom_push(key='data', value=df_json)
    logger.info(f"Transformed DataFrame: {df}")

def load(**kwargs):
    logger.info("Starting load task")
    df_json = kwargs['ti'].xcom_pull(key='data', task_ids='transform')
    df = pd.read_json(df_json, orient='split')
    output_path = os.getenv("OUTPUT_PATH")
    host_airflow_path = os.getenv("HOST_AIRFLOW_PATH")
    container_output_path = output_path.replace(host_airflow_path, '/host/airflow')
    logger.info(f"Output path from .env: {container_output_path}")
    if not container_output_path:
        logger.error("Output path is not set. Please check your .env file.")
        raise ValueError("Output path is not set")
    
    df.to_csv(container_output_path, index=False)
    logger.info(f"DataFrame successfully written to {container_output_path}")
    logger.info(f"Final DataFrame: {df}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 16),
    'retries': 1,
}

with DAG('simple_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
        provide_context=True
    )
    
    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
        provide_context=True
    )
    
    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
        provide_context=True
    )

    extract_task >> transform_task >> load_task
