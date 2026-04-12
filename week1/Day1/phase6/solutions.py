from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("Phase6_Full").getOrCreate()

# LOAD DATA

customers_data = [
    (1, "John Doe", "john@example.com", "Hyderabad"),
    (2, "Alice ", "alice@example.com", "Chennai"),
    (3, None, "bob@example.com", "Bangalore"),
    (4, "David", None, "Mumbai"),
    (5, "Eva", "eva@example.com", "Hyderabad"),
    (6, "Frank", "frank@example.com", "Delhi"),
]
customers = spark.createDataFrame(customers_data, ["customer_id", "name", "email", "city"])

orders_data = [
    (101, 1, "2024-01-01", 1000),
    (102, 2, "2024-01-02", 2000),
    (103, 3, "2024-01-03", -500),
    (104, 99, "2024-01-04", 1500),
    (105, 1, "2024-01-05", None),
    (106, 5, "2024-01-06", 3000),
    (107, 5, "2024-01-07", 3000),
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "order_date", "amount"])

orders = orders.withColumn("order_date", to_date(col("order_date")))

# CLEAN DATA

customers_clean = customers.withColumn("name", trim(col("name"))) \
                           .dropna(subset=["name", "email"])

orders_clean = orders.filter((col("amount").isNotNull()) & (col("amount") > 0))

# JOIN DRILLS (Practice A)

# Inner Join
inner_join_df = orders_clean.join(customers_clean, "customer_id", "inner")

# Left Join
left_join_df = orders_clean.join(customers_clean, "customer_id", "left")

# Left Anti Join (Invalid FK)
invalid_orders = orders_clean.join(customers_clean, "customer_id", "left_anti")

print("Invalid Orders:")
invalid_orders.show()

# Row Count Comparison
print("Inner Join Count:", inner_join_df.count())
print("Left Join Count:", left_join_df.count())
print("Invalid Orders Count:", invalid_orders.count())

# FINAL VALID DATA

final_df = inner_join_df

# AGGREGATIONS

agg_df = final_df.groupBy("customer_id", "name", "city") \
    .agg(
        sum("amount").alias("total_spend"),
        count("order_id").alias("order_count")
    )

# WINDOW FUNCTIONS (Practice B)

# Rank customers by total spend
rank_window = Window.orderBy(desc("total_spend"))
ranked_df = agg_df.withColumn("rank", rank().over(rank_window))

# Top 3 customers per city
city_window = Window.partitionBy("city").orderBy(desc("total_spend"))
top3_df = agg_df.withColumn("city_rank", rank().over(city_window)) \
                .filter(col("city_rank") <= 3)

# Running total of sales
running_window = Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding, 0)
running_df = final_df.withColumn("running_total", sum("amount").over(running_window))

# LAG function (previous order amount)
lag_window = Window.partitionBy("customer_id").orderBy("order_date")
lag_df = final_df.withColumn("prev_amount", lag("amount", 1).over(lag_window))

# DATE ANALYSIS (Practice C)

# Extract month
date_df = final_df.withColumn("month", month("order_date"))

# Monthly sales aggregation
monthly_sales = date_df.groupBy("month") \
    .agg(sum("amount").alias("monthly_total"))

# Date difference (example: days from first order)
date_diff_df = final_df.withColumn(
    "days_diff",
    datediff(col("order_date"), lit("2024-01-01"))
)

# SHOW RESULTS

print("Ranked Customers:")
ranked_df.show()

print("Top 3 Customers per City:")
top3_df.show()

print("Running Total:")
running_df.show()

print("LAG Results:")
lag_df.show()

print("Monthly Sales:")
monthly_sales.show()

# SAVE OUTPUT
ranked_df.write.mode("overwrite").csv("/tmp/phase6_output")


## Reflection Questions

1. Which task took the most time?

The most time-consuming task was implementing **quantile-based segmentation in SQL**. Unlike PySpark, MySQL (especially older versions) does not support advanced functions like `NTILE()`, so I had to try different approaches and adjust the logic manually.

2. What mistakes did you make?
I made a few mistakes during the process:
* Used unsupported SQL functions like `NTILE()` in MySQL
* Referred to incorrect column names(e.g., `JoinDate` instead of `date`).
* Tried creating views with unsupported syntax.
* Faced issues with data types and formats (dates).

3. How did you debug issues?
I debugged issues by:
* Carefully reading the **error messages.
* Checking column names using SELECT statements.
* Running queries step-by-step instead of all at once.
* Simplifying logic when advanced functions were not supported
* Verifying intermediate outputs before moving forward

4. Can you now build pipeline independently?

Yes, I can now build a basic **ETL pipeline independently**. I understand how to:

* Extract data into tables
* Clean and transform data
* Perform aggregations and joins
* Create segmentation logic
* Generate final reports

5. What needs improvement?

I still need to improve in :
* Writing optimized SQL queries.
* Handling different database versions and compatibility issues.
* Using more advanced functions and window operations.
* Improving debugging speed and efficiency.


