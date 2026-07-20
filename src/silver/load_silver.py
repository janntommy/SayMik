from pyspark.sql import functions

def build_silver(year: int, month: int) -> None:
    bronze_data = f"db_saymik.bronze.votings_raw_{year}_{month:02d}"
    silver_data = f"db_saymik.silver.votings_{year}_{month:02d}"

    df = spark.table(bronze_data)

    df_silver = (df
                 .withColumn("date", functions.to_timestamp("date"))
                 .drop("links")
                 )

    df_silver.write.mode("overwrite").format("delta").saveAsTable(silver_data)
    print("Silver table saved successfully.")

build_silver(2026,6)