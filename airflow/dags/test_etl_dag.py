from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

def extract(**kwargs):
    # Create a dummy dataframe
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': ['A', 'B', 'C']
    })
    # Push the dataframe to XCom
    kwargs['ti'].xcom_push(key='data', value=df.to_dict())

def transform(**kwargs):
    # Pull the dataframe from XCom
    df_dict = kwargs['ti'].xcom_pull(key='data', task_ids='extract')
    df = pd.DataFrame.from_dict(df_dict)
    # Add a last_modified column
    df['last_modified'] = datetime.now()
    # Push the transformed dataframe to XCom
    kwargs['ti'].xcom_push(key='data', value=df.to_dict())

def load(**kwargs):
    # Pull the transformed dataframe from XCom
    df_dict = kwargs['ti'].xcom_pull(key='data', task_ids='transform')
    df = pd.DataFrame.from_dict(df_dict)
    # Save the dataframe to a CSV file
    df.to_csv('/path/to/your/output.csv', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('simple_etl_dag', default_args=default_args, schedule_interval='@daily') as dag:
    
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
