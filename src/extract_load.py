from bcb import sgs
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = (
    SparkSession.builder.appName("metricas_economicas_bronze")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()

selic = sgs.get({'selic': 432}, start='2000-01-01')
selic.reset_index(inplace=True)
selic.rename(columns={'date': 'date', 'selic': 'value'}, inplace=True)
selic['indicador'] = 'SELIC'
df_selic = spark.createDataFrame(selic)
print(df_selic)
#df_selic.write.format("delta").mode("overwrite").save(r"C:\Users\vidal\Documents\workspace\economic_simulator\data\bronze\selic.delta")
