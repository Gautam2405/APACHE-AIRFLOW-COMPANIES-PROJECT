# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 6, 13),
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
# }

# dag = DAG(
#     'simple_data_pipeline',
#     default_args=default_args,
#     description='A simple data pipeline using PythonOperator',
#     schedule_interval='@daily',
# )

# def extract_data():
#     print("Extracting data...")
#     # Your data extraction code here

# def transform_data():
#     print("Transforming data...")
#     # Your data transformation code here

# def load_data():
#     print("Loading data...")
#     # Your data loading code here

# extract_task = PythonOperator(
#     task_id='extract_data',
#     python_callable=extract_data,
#     dag=dag,
# )

# transform_task = PythonOperator(
#     task_id='transform_data',
#     python_callable=transform_data,
#     dag=dag,
# )

# load_task = PythonOperator(
#     task_id='load_data',
#     python_callable=load_data,
#     dag=dag,
# )

# # Define the task dependencies
# extract_task >> transform_task >> load_task


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'simple_data_pipeline',
    default_args=default_args,
    description='A simple data pipeline using PythonOperator',
    schedule='@daily',  # Updated parameter name
)

def extract_data():
    print("Extracting data...")
    # Your data extraction code here

def transform_data():
    print("Transforming data...")
    # Your data transformation code here

def load_data():
    print("Loading data...")
    # Your data loading code here

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

# Define the task dependencies
extract_task >> transform_task >> load_task
