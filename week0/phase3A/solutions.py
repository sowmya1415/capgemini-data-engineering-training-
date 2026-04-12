from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

spark = SparkSession.builder.getOrCreate()

# -------------------------
# CREATE DATAFRAME
# -------------------------
data = [
    (1, "Ravi", "Hyderabad", 25),
    (2, None, "Chennai", 32),
    (None, "Arun", "Hyderabad", 28),
    (4, "Meena", None, 30),
    (4, "Meena", None, 30),
    (5, "John", "Bangalore", -5)
]

columns = ["customer_id", "name", "city", "age"]

df = spark.createDataFrame(data, columns)

# -------------------------
# ORIGINAL COUNT
# -------------------------
print("Original Rows:", df.count())

# -------------------------
# CLEANING
# -------------------------
clean_df = df.dropna(subset=["customer_id"])

clean_df = clean_df.fillna({
    "name": "Unknown",
    "city": "Unknown"
})

clean_df = clean_df.dropDuplicates()

clean_df = clean_df.filter(col("age") > 0)

# -------------------------
# CLEANED COUNT
# -------------------------
print("Cleaned Rows:", clean_df.count())

# -------------------------
# FINAL DATA
# -------------------------
clean_df.show()

# -------------------------
# AGGREGATION (Customers per City)
# -------------------------
clean_df.groupBy("city") \
        .agg(count("customer_id").alias("customer_count")) \
        .show()