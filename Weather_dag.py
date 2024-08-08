from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from pipeline import fetch_and_store_weather_data

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'weather_data_fetch',
    default_args=default_args,
    description='Fetch weather data every 24 hours',
    schedule_interval=timedelta(days=1),  # Run every 24 hours
)

# Define the task using PythonOperator
fetch_weather_data_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_and_store_weather_data,  # Call the function from your script
    dag=dag,
)

# Set the task
fetch_weather_data_task
