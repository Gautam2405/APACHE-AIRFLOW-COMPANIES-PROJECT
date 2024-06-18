# APACHE-AIRFLOW-COMPANIES-PROJECT
Create a data pipeline using Apache Airflow to process a company dataset from Kaggle. The pipeline involves data exploration, filtering, and loading the processed data into a database (Excel, SQL, PL/SQL, MongoDB). This project demonstrates setting up Airflow, defining DAGs, and performing ETL operations.


# Data Pipeline with Apache Airflow

This project demonstrates how to set up a data pipeline using Apache Airflow to process a company dataset from Kaggle. The pipeline includes data exploration, filtering, and loading the processed data into a database.

## Table of Contents
- [Project Overview]:
This project demonstrates how to set up a data pipeline using Apache Airflow to process a company dataset from Kaggle. The pipeline includes data exploration, filtering, and loading the processed data into a database. The main goal is to automate the data processing workflow using Apache Airflow, ensuring efficient data handling and storage.


  
- [Installation]:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Install and set up Apache Airflow:
    ```bash
    pip install apache-airflow
    airflow db init
    ```
  
- [Usage]:
1. Start the Airflow web server and scheduler:
    ```bash
    airflow webserver --port 8080
    airflow scheduler
    ```

2. Access the Airflow UI at `http://localhost:8080` to monitor and manage your DAGs.


- [Pipeline Details]:
The Airflow DAG for this project includes the following tasks:

1. **Data Extraction**: Download and explore the dataset from Kaggle using Pandas.
2. **Data Transformation**: Filter the dataset to extract useful information.
3. **Data Loading**: Load the filtered data into the chosen database (Excel, SQL, PL/SQL, MongoDB).

Each task in the DAG is defined using the `PythonOperator` to execute Python code


- [Database Setup]:
## Database Setup
Depending on the chosen database system, follow these steps to set up the database:

### MongoDB
1. Start the MongoDB service:
    ```bash
    sudo systemctl start mongod
    sudo systemctl enable mongod
    sudo systemctl status mongod
    ```

2. Access the MongoDB shell:
    ```bash
    mongo
    ```

### SQL Databases
1. Install the necessary libraries (e.g., SQLAlchemy, psycopg2, cx_Oracle).
2. Configure the database connection in your Airflow tasks.


- [Commands]:
Here are some useful commands for managing the project:

``bash
- Navigate to the Airflow directory
cd /home/gautam/airflow

- Run the main Python script
python3 main.py

- Start the Airflow scheduler and web server in detached mode
airflow scheduler 
airflow webserver 


- [Contributing]
Explain how others can contribute to the project.

``markdown
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions. Follow the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.


- [License]:
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

  
- [Contact]:
Gautam - (email:gautampankuta339@gmail.com)


## Project Overview
This project outlines the steps to create a data pipeline using Apache Airflow. The pipeline involves:
1. Downloading and exploring a company dataset from Kaggle.
2. Setting up Apache Airflow.
3. Creating an Airflow Directed Acyclic Graph (DAG) to manage the data pipeline.
4. Loading filtered data into a chosen database (Excel, SQL, PL/SQL, MongoDB).
5. Testing and monitoring the pipeline.

## Installation
Follow these steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Install and set up Apache Airflow:
    ```bash
    pip install apache-airflow
    airflow db init
    ```

## Usage
1. Start the Airflow web server and scheduler:
    ```bash
    airflow webserver --port 8080
    airflow scheduler
    ```

2. Access the Airflow UI at `http://localhost:8080` to monitor and manage your DAGs.

## Pipeline Details
The Airflow DAG for this project includes the following tasks:
1. **Data Extraction**: Download and explore the dataset from Kaggle using Pandas.
2. **Data Transformation**: Filter the dataset to extract useful information.
3. **Data Loading**: Load the filtered data into the chosen database.

Each task in the DAG is defined using the `PythonOperator` to execute Python code.

## Database Setup
Depending on the chosen database system, follow these steps to set up the database:

### MongoDB
1. Start the MongoDB service:
    ```bash
    sudo systemctl start mongod
    sudo systemctl enable mongod
    sudo systemctl status mongod
    ```

2. Access the MongoDB shell:
    ```bash
    mongo
    ```

### SQL Databases
1. Install the necessary libraries (e.g., SQLAlchemy, psycopg2, cx_Oracle).
2. Configure the database connection in your Airflow tasks.

## Commands
Here are some useful commands for managing the project:

```bash
# Navigate to the Airflow directory
cd /home/gautam/airflow

# Run the main Python script
python3 main.py

# Start the Airflow scheduler and web server in detached mode
airflow scheduler -D
airflow webserver -D
