from pyspark.sql import Window
from pyspark.ml.feature import Bucketizer
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark session
spark=SparkSession.builder.appName("app").getOrCreate()

# Read datasets
customers=spark.read.format("csv").option("header","true").option("inferSchema","true").load("/samples/customers.csv")
sales=spark.read.format('csv').option("header","true").option("inferSchema", "true").load("/samples/sales.csv")

# Clean data (remove nulls, duplicates, invalid values)
customers=customers.dropna(subset=["customer_id"]).dropDuplicates(["customer_id"])
sales = sales.dropna(subset=["customer_id"]).dropDuplicates(["sale_id"]).filter(col("total_amount") > 0)

# Join sales and customers
df = sales.join(customers, "customer_id")

# Create full name column
name = df.withColumn(
    "full_name",
    concat_ws(" ", col("first_name"), col("last_name"))
)

# Calculate total spend per customer
amount=name.groupby("full_name").agg(sum("total_amount").alias("total_spend"))

# 1️ Fixed rule-based segmentation
# Apply business logic:
# >100 → Gold
# 50–100 → Silver
# <50 → Bronze
segment=amount.withColumn("segmentation",
    when(col("total_spend")>100,"gold")
    .when((col("total_spend") >= 50) & (col("total_spend") <= 100), "Silver")
    .otherwise("Bronze"))

segment.select("full_name", "total_spend", "segmentation").show()

# 2️ Count customers in each segment
segment.groupby("segmentation").agg(count(col("full_name"))).show()

# 3️ Quantile-based segmentation
# Find 33% and 66% thresholds dynamically
q1,q1=amount.approxQuantile("total_spend", [0.33, 0.66], 0)

# Segment based on quantiles
quantile=amount.withColumn("segment2",
    when(col("total_spend")<q1,"bronze")
    .when(col("total_spend")<q1,"silver")
    .otherwise("gold"))

quantile.select("full_name", "total_spend", "segment2").show()

#  Other Method 1: Window (Percent Rank)
# Rank customers based on spend percentage
window = Window.orderBy("total_spend")

rank= amount.withColumn("rank_pct", percent_rank().over(window))

# Assign segment based on rank percentage
df_window = rank.withColumn(
    "segment_rank",
    when(col("rank_pct") <= 0.33, "Bronze")
     .when(col("rank_pct") <= 0.66, "Silver")
     .otherwise("Gold")
)

display(df_window.select("full_name", "total_spend", "rank_pct", "segment_rank"))


# Other Method 2: Bucketizer

# Define fixed ranges (bins)
splits = [-float("inf"), 5000, 10000, float("inf")]

# Convert numeric column into buckets
bucketizer = Bucketizer(splits=splits, inputCol="total_spend", outputCol="bucket")
bucket= bucketizer.transform(amount)

# Map bucket values to segments
df_bucket =bucket.withColumn(
    "segment_bucket",
    when(col("bucket") == 0, "Bronze")
     .when(col("bucket") == 1, "Silver")
     .otherwise("Gold")
)

display(df_bucket.select("full_name", "total_spend", "segment_bucket"))


# 4️Compare all segmentation methods

comparison = segment \
    .join(quantile.select("full_name", "segment2"), "full_name") \
    .join(df_bucket.select("full_name", "segment_bucket"), "full_name") \
    .join(df_window.select("full_name", "segment_rank"), "full_name")

# Show comparison of all methods
display(comparison.select(
    "full_name",
    "total_spend",
    "segmentation",
    "segment2",
    "segment_bucket",
    "segment_rank"
))