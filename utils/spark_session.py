from pyspark.sql import SparkSession

def create_spark_session(appName="World Bank Analysis App"):
    spark = SparkSession\
            .builder\
            .appName(appName)\
            .config("spark.sql.shuffle.partitions","2")\
            .getOrCreate()
    return spark