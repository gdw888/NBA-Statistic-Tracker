from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
    'nba_stats_scrapy',
    default_args=default_args,
    description='A simple Scrapy DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:
    
    run_scrapy_spider = BashOperator(
        task_id='run_scrapy_spider',
        bash_command='scrapy crawl player_stats -o /path/to/output/player_stats.json',
        dag=dag,
    )

    run_scrapy_spider