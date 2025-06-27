from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta
import requests
import logging

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(seconds=30),
}

def get_btc_price_and_notify():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        price = response.json()['bitcoin']['usd']
        message = f"Current BTC price: ${price}"
        logging.info(message)

        # Send Email
        send_email(
            to=["your-email@example.com"],
            subject="BTC Price Update",
            html_content=f"<p>{message}</p>"
        )

    except Exception as e:
        logging.error(f"Failed to get BTC price: {e}")

with DAG(
    dag_id='btc_price_notifier_minutely',
    default_args=default_args,
    description='Fetch and email BTC price every minute',
    schedule_interval='* * * * *',
    start_date=datetime(2025, 6, 27),
    catchup=False,
    tags=['crypto'],
) as dag:

    fetch_and_notify = PythonOperator(
        task_id='get_btc_price_and_notify_task',
        python_callable=get_btc_price_and_notify
    )

    fetch_and_notify
