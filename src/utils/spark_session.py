#spark session

from pyspark.sql import SparkSession


def get_spark_session(app_name):
    return (SparkSession.builder
            .appName(app_name)
            .config("spark.sql.adaptive.enabled", "true")
            .config("spark.sql.shuffle.partitions", "200")
            .getOrCreate())