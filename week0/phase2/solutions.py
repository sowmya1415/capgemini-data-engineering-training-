from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count, col

spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

customers_data = [
    ("1", "Amit", "Hyderabad"),
    ("2", "Sneha", "Bangalore"),
    ("3", "Rahul", "Chennai"),
    ("4", "Priya", "Hyderabad")
]

customers = spark.createDataFrame(customers_data, ["customer_id", "name", "city"])

orders_data = [
    ("101", "1", 500),
    ("102", "1", 300),
    ("103", "2", 700),
    ("104", "3", 200),
    ("105", "3", 100)
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "amount"])

# 1. Total order amount for each customer

orders.groupBy("customer_id") \
      .agg(sum("amount").alias("total_amount")) \
      .show()

# 2. Top 3 customers by total spend

orders.groupBy("customer_id") \
      .agg(sum("amount").alias("total_spend")) \
      .orderBy("total_spend", ascending=False) \
      .limit(3) \
      .show()


# 3. Customers with no orders

customers.join(orders, "customer_id", "left") \
         .filter(col("order_id").isNull()) \
         .show()

# 4. City-wise total revenue

customers.join(orders, "customer_id") \
         .groupBy("city") \
         .agg(sum("amount").alias("total_revenue")) \
         .show()

# 5. Average order amount per customer

orders.groupBy("customer_id") \
      .agg(avg("amount").alias("avg_amount")) \
      .show()


# 6. Customers with more than one order

orders.groupBy("customer_id") \
      .agg(count("order_id").alias("order_count")) \
      .filter(col("order_count") > 1) \
      .show()

# 7. Sort customers by total spend descending
orders.groupBy("customer_id") \
      .agg(sum("amount").alias("total_spend")) \
      .orderBy("total_spend", ascending=False) \
      .show()
