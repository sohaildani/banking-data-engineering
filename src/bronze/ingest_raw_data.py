from utils.spark_session import get_spark_session


spark = get_spark_session("Bronze Ingestion")


customers = spark.read.option("header", True).csv("data/raw/customers.csv")
accounts = spark.read.option("header", True).csv("data/raw/accounts.csv")
transactions = spark.read.option("header", True).csv("data/raw/transactions.csv")


customers.write.mode("append").parquet("data/bronze/customers")
accounts.write.mode("append").parquet("data/bronze/accounts")
transactions.write.mode("append").parquet("data/bronze/transactions")