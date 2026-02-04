#!/bin/bash


set -e


echo "Running Bronze Layer"
spark-submit src/bronze/ingest_raw_data.py


echo "Running Silver Layer"
spark-submit src/silver/clean_customers.py
spark-submit src/silver/clean_accounts.py
spark-submit src/silver/scd2_customers.py


echo "Running Gold Layer"
spark-submit src/gold/customer_kpis.py


echo "Pipeline completed successfully"