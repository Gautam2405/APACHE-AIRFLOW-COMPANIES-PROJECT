from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pymongo import MongoClient

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 14),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'load_data_to_mongodb',
    default_args=default_args,
    description='A simple DAG to load data into MongoDB',
    schedule=timedelta(days=1),
)

def load_data_to_mongodb(**kwargs):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mydatabase']
    collection = db['mycollection']

    # Example filtered data
    filtered_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
    ]

    # Insert the filtered data into MongoDB
    collection.insert_many(filtered_data)

    # Close the connection
    client.close()

# Define the PythonOperator to load data into MongoDB
load_data_task = PythonOperator(
    task_id='load_data_to_mongodb_task',
    python_callable=load_data_to_mongodb,
    dag=dag,
)

# Set the task dependencies
load_data_task
