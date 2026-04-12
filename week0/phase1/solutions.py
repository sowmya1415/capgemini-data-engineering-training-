from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Phase1").getOrCreate()

customers = spark.createDataFrame([
    (1, "Ravi", "Hyderabad", 25),
    (2, "Sita", "Chennai", 32),
    (3, "Arun", "Hyderabad", 28)
], ["customer_id", "customer_name", "city", "age"])

# 1. Show all customers
customers.show()

# 2. Show customers from Chennai
customers.filter(customers.city == "Chennai").show()

# 3. Show customers with age > 25
customers.filter(customers.age > 25).show()

# 4. Show only customer_name and city
customers.select("customer_name", "city").show()

# 5. Count customers city-wise
customers.groupBy("city").count().show()
