from pyspark.sql.functions import col
from src.utils.spark_session import get_spark_session


spark = get_spark_session("Clean Accounts")


df = spark.read.parquet("data/bronze/accounts")


df_clean = df.filter(col("balance") >= 0)


df_clean.write.mode("overwrite").parquet("data/silver/accounts")