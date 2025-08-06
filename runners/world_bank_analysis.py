from utils.spark_session import create_spark_session
from schema.world_bank_schema import data_schema

file_path = "data/world_bank_dataset.csv"

spark = create_spark_session("Analysis")



def run_sql_queries(query_file_path):
    world_bank_data = spark.read.format("csv")\
                        .option("header",True)\
                        .schema(data_schema)\
                        .load(file_path)
    world_bank_data.show(10)
    world_bank_data.printSchema()

    # world bank view
    world_bank_data.createOrReplaceTempView("world_bank_dataset")

    # read and run sql queries
    with open(query_file_path,"r") as file:
        query = file.read()
        print(f"\nRunning query from: {query_file_path}")
        print(f"Query:\n{query}")


    query_result = spark.sql(str(query))
    query_result.show(truncate=False)

 # query file paths
query_file_paths = [
    "queries/unemployment_rate_per.sql",
    "queries/top_5_gdp.sql",
    "queries/lowest_electricity_access.sql",
    "queries/co2_emission.sql",
    "queries/average_life_expectancy.sql",
]

for path in query_file_paths:
    run_sql_queries(path)


                        


