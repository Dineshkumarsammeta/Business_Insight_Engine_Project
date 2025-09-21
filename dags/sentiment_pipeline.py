"""
Airflow DAG: sentiment_pipeline
Purpose: Demonstrate ETL and ML workflow for real-time sentiment analysis.
Workflow: ingest -> validate schema -> Spark transform -> model predict -> metrics push
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import time
import random
import json

# Default arguments
default_args = {
    'owner': 'sammeta',
    'depends_on_past': False,
    'start_date': datetime(2025, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'sentiment_pipeline',
    default_args=default_args,
    description='ETL + ML pipeline for real-time sentiment analysis',
    schedule_interval='@daily',  # daily run; adjust as needed
    catchup=False
)

# Dummy functions for each step
def ingest():
    """Simulate data ingestion"""
    data = [
        {"text": "I love this product!", "timestamp": str(datetime.now())},
        {"text": "Service was slow.", "timestamp": str(datetime.now())}
    ]
    with open('/tmp/ingest.json', 'w') as f:
        for row in data:
            f.write(json.dumps(row) + "\n")
    print("Ingested 2 messages")

def validate_schema():
    """Simulate schema validation"""
    df = pd.read_json('/tmp/ingest.json', lines=True)
    assert 'text' in df.columns and 'timestamp' in df.columns
    print("Schema validated")

def spark_transform():
    """Simulate Spark transformation"""
    df = pd.read_json('/tmp/ingest.json', lines=True)
    df['text_length'] = df['text'].apply(len)
    df.to_csv('/tmp/transformed.csv', index=False)
    print("Transformation complete")

def model_predict():
    """Simulate ML model prediction"""
    df = pd.read_csv('/tmp/transformed.csv')
    # Random sentiment for demo
    df['sentiment'] = df['text'].apply(lambda x: random.choice(['positive', 'neutral', 'negative']))
    df.to_csv('/tmp/predictions.csv', index=False)
    print("Predictions complete")

def metrics_push():
    """Simulate metrics push"""
    df = pd.read_csv('/tmp/predictions.csv')
    metrics = {
        'run_date': str(datetime.now()),
        'dataset': 'simulated',
        'method': 'demo-model',
        'accuracy': 0.85,
        'f1_macro': 0.83,
        'n_samples': len(df)
    }
    pd.DataFrame([metrics]).to_csv('/tmp/metrics.csv', index=False)
    print("Metrics pushed:", metrics)

# Define tasks
t1 = PythonOperator(task_id='ingest', python_callable=ingest, dag=dag)
t2 = PythonOperator(task_id='validate_schema', python_callable=validate_schema, dag=dag)
t3 = PythonOperator(task_id='spark_transform', python_callable=spark_transform, dag=dag)
t4 = PythonOperator(task_id='model_predict', python_callable=model_predict, dag=dag)
t5 = PythonOperator(task_id='metrics_push', python_callable=metrics_push, dag=dag)

# Task dependencies
t1 >> t2 >> t3 >> t4 >> t5
