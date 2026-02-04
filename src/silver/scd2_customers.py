from pyspark.sql.functions import col, lit, lead
from pyspark.sql.window import Window
from utils.spark_session import get_spark_session


spark = get_spark_session("SCD2 Customers")


df = spark.read.parquet("data/silver/customers")


window = Window.partitionBy("customer_id").orderBy("updated_at")


scd2 = (df
.withColumn("effective_from", col("updated_at"))
.withColumn("effective_to", lead("updated_at").over(window))
.withColumn("is_current", col("effective_to").isNull()))


scd2.write.mode("overwrite").parquet("data/silver/customers_scd2")