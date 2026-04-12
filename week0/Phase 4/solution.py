from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark session
spark=SparkSession.builder.appName("app").getOrCreate()

# Read sales and customers datasets
sales=spark.read.format('csv').option("header","true").option("inferSchema", "true").load("/samples/sales.csv")
customers=spark.read.format('csv').option("header","true").option("inferSchema", "true").load("/samples/customers.csv")

# 1️ Daily sales calculation
# Group by sale_date and calculate total sales per day

sales.groupby("sale_date").agg(sum("total_amount")).show()


# 2️ City-wise revenue 
# Group by city and calculate total amount

sales.groupby("city").agg(sum("total_amount")).show()


# 3️ Top 5 customers (lowest spend)
# Join sales and customers → create full name → calculate total spend
# Sort ascending → get lowest 5 customers

sales.join(customers,"customer_id","left") \
.groupby(concat_ws(" ","first_name","last_name")) \
.agg(sum("total_amount").alias("total")) \
.orderBy("total",ascending=True) \
.limit(5) \
.show()


# 4️ Repeat customers (>1 order)
# Group by customer_id → count orders → filter customers with more than 1 order

sales.groupby("customer_id") \
.agg(count("sale_id").alias("total_orders")) \
.filter(col("total_orders")>1) \
.show()

# 5️ Customer Segmentation
# Join data → create full name → calculate total spend
# Apply business logic (Gold, Silver, Bronze)

from pyspark.sql.functions import col, sum, when, concat_ws

df = sales.join(customers, "customer_id")

name = df.withColumn("full_name", concat_ws(" ", col("first_name"), col("last_name")))

money = name.groupBy("full_name") \
    .agg(sum("total_amount").alias("total_spend"))

segmentation = money.withColumn(
    "segment",
    when(col("total_spend") > 10000, "Gold")
    .when((col("total_spend") >= 5000) & (col("total_spend") <= 10000), "Silver")
    .otherwise("Bronze")
)

segmentation.select("full_name", "total_spend", "segment").show()


# 6️ Final Reporting Table
# Join data → create full name → calculate total spend + order count
# Apply segmentation logic

from pyspark.sql.functions import *

df = sales.join(customers, "customer_id")

# Create full name column
name = df.withColumn("full_name", concat_ws(" ", col("first_name"), col("last_name")))

# Aggregate total spend and number of orders
agg_df = name.groupBy("full_name", "city") \
    .agg(
        sum("total_amount").alias("total_spend"),
        count("sale_id").alias("order_count")
    )

# Apply segmentation (Gold, Silver, Bronze)
segmentation = agg_df.withColumn(
    "segment",
    when(col("total_spend") > 10000, "Gold")
    .when((col("total_spend") >= 5000) & (col("total_spend") <= 10000), "Silver")
    .otherwise("Bronze")
)