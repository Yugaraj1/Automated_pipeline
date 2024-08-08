Automated Weather Data Pipeline with MySQL
Overview
This project fetches weather data from the Weatherstack API for a predefined list of 200 cities and uploads the data to a MySQL database. The process is scheduled to run every 24 hours using Apache Airflow.

How It Works
City List: Uses a list of 200 cities.
API Request: Retrieves weather data from Weatherstack API.
Data Transformation: Converts data into a pandas DataFrame.
Data Insertion: Inserts data into a MySQL table.
Scheduling: Uses Airflow to automate the process every 24 hours.
Setup
Prerequisites
Python 3.x
MySQL Server
Apache Airflow
Python Packages
Install the required Python packages using pip:

bash
Copy code
pip install pandas requests sqlalchemy pymysql apache-airflow
Configuration
Create the Python Script

Save your weather data fetching and uploading script to a file (e.g., fetch_weather_data.py).

Schedule with Airflow

Define an Airflow DAG to run your script every 24 hours and place it in your Airflow DAGs directory.

Run Airflow

Start the Airflow web server and scheduler:

bash
Copy code
airflow webserver --port 8080
airflow scheduler
Notes
API Key: Replace 'your_weatherstack_api_key' in your script with your actual Weatherstack API key.
City List: Update the list of cities in your script as needed.
Database Connection: Ensure the MySQL connection string in your script matches your database setup.
