from utils.spark_session import create_spark_session
from schema.world_bank_schema import data_schema

file_path = "data/world_bank_dataset.csv"

spark = create_spark_session("Analysis")

world_bank_data = spark.read.format("csv")\
                        .option("header",True)\
                        .schema(data_schema)\
                        .load(file_path)
                        


world_bank_data.show(10)
world_bank_data.printSchema()