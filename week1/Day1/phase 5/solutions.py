# Task 1: calculate total spend and rank top 3 customers per city
from pyspark.sql.functions import sum as _sum
from pyspark.sql.window import Window
from pyspark.sql.functions import dense_rank

# total spend per customer per city
amount = fact_orders.groupBy("customer_id", "customer_city") \
    .agg(_sum("payment_value").alias("total_spend"))

# window for ranking inside each city
window_spec = Window.partitionBy("customer_city").orderBy(col("total_spend").desc())

# assign rank and filter top 3
top_customers = amount.withColumn("rank", dense_rank().over(window_spec)) \
    .filter(col("rank") <= 3)

display(top_customers.select(
    col("customer_city").alias("city"),
    "customer_id",
    "total_spend",
    "rank"
))


# Task 2: calculate daily sales and running total
from pyspark.sql.functions import to_date

# convert timestamp to date and sum daily sales
daily_sales = fact_orders.withColumn("date", to_date("order_purchase_timestamp")) \
    .groupBy("date") \
    .agg(_sum("payment_value").alias("daily_sales"))

# window for cumulative sum
window_spec = Window.orderBy("date").rowsBetween(Window.unboundedPreceding, 0)

# running total calculation
running_sales = daily_sales.withColumn(
    "running_total",
    _sum("daily_sales").over(window_spec)
)

display(running_sales)


# Task 3: calculate total sales and rank products per category

# total sales per product
product_sales = fact_orders.groupBy("product_id", "product_category_name") \
    .agg(_sum("payment_value").alias("total_sales"))

# window for ranking products in each category
window_spec = Window.partitionBy("product_category_name") \
    .orderBy(col("total_sales").desc())

# assign rank
ranked_products = product_sales.withColumn(
    "rank",
    dense_rank().over(window_spec)
)

display(ranked_products.select(
    col("product_category_name").alias("category"),
    "product_id",
    "total_sales",
    "rank"
))


# Task 4: calculate total spend per customer (CLV)
clv = fact_orders.groupBy("customer_id") \
    .agg(_sum("payment_value").alias("total_spend"))

display(clv)


# Task 5: segment customers based on spend and count them
from pyspark.sql.functions import when

# create segment column
segmentation = clv.withColumn(
    "segment",
    when(col("total_spend") > 100, "Gold")
    .when((col("total_spend") >= 50) & (col("total_spend") <= 100), "Silver")
    .otherwise("Bronze")
)

# count customers per segment
segment_count = segmentation.groupBy("segment").count()

display(segmentation)
display(segment_count)


# Task 6: create final report with all details

# count total orders per customer
orders_count = fact_orders.groupBy("customer_id") \
    .count() \
    .withColumnRenamed("count", "total_orders")

# get customer city
customer_city = fact_orders.select("customer_id", "customer_city").distinct()

# join all results
final_report = segmentation \
    .join(customer_city, "customer_id", "left") \
    .join(orders_count, "customer_id", "left")

display(final_report.select(
    "customer_id",
    col("customer_city").alias("city"),
    "total_spend",
    "segment",
    "total_orders"
))