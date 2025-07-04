﻿# 🪙 Airflow BTC Price Notifier

This project sets up an Apache Airflow DAG that fetches the current Bitcoin (BTC) price every minute using the CoinGecko API and sends the result via email.

## 📦 Features

- 🕒 Runs every minute
- 🌐 Uses the CoinGecko public API
- 📧 Sends BTC price to your email

```bash
sudo apt update && sudo apt install python3-pip
pip install apache-airflow
export AIRFLOW_HOME=~/airflow
airflow db init
airflow webserver --port 8080 &
airflow scheduler &
```

Visit http://localhost:8080 
