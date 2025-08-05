from pyspark.sql.types import StructType,StructField,IntegerType,FloatType,StringType

data_schema = StructType([
    StructField("Country", StringType(), True),
    StructField("Year", IntegerType(), True),
    StructField("GDP_USD", IntegerType(), True),
    StructField("Population",IntegerType(),True),
    StructField("Life_Expectancy",IntegerType(),True),
    StructField("Unemployment_Rate",FloatType(),True),
    StructField("CO2_Emission",FloatType(),True),
    StructField("Electricity_Access",FloatType(),True),
    

    ])