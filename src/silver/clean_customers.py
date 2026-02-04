from pyspark.sql.functions import col, to_date
from utils.spark_session import get_spark_session


spark = get_spark_session("Silver Customers")


df = spark.read.parquet("data/bronze/customers")


df_clean = (df
.withColumn("dob", to_date(col("dob")))
.dropDuplicates(["customer_id", "updated_at"]))


df_clean.write.mode("overwrite").parquet("data/silver/customers")