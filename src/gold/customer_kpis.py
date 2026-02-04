from pyspark.sql.functions import sum
from utils.spark_session import get_spark_session


spark = get_spark_session("Gold KPIs")


accounts = spark.read.parquet("data/silver/accounts")
transactions = spark.read.parquet("data/bronze/transactions")


kpi = (transactions
.groupBy("account_id")
.agg(sum("amount").alias("net_amount")))


kpi.write.mode("overwrite").parquet("data/gold/account_kpis")