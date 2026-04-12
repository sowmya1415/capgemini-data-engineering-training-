# Car Sales Data Pipeline (PySpark + SQL)

# Objective

Build an end-to-end data pipeline using PySpark and SQL to perform data ingestion, cleaning, validation, transformation, and analytical reporting on car sales data.

# Dataset Overview

The pipeline works with the following datasets:

customers (customer_id, name, city)
cars (car_id, brand, model, price)
sales (sale_id, customer_id, car_id, sale_date, quantity)
dealers (dealer_id, name, city)
sales_dealer (sale_id, dealer_id)
# Tech Stack
PySpark – Data processing & transformations
SQL – Analytical queries
# Databricks Community Edition – Execution environment
 # Pipeline Architecture
Raw Data → Data Cleaning → Validation → Transformation → SQL Analysis → Output
# Phase 1 – Data Understanding
Tasks Performed:
Loaded datasets into PySpark DataFrames
Inspected schema using printSchema()
Performed initial data profiling
Issues Identified:
Null values in columns (e.g., customer name)
Negative values in price
Invalid foreign keys (e.g., unmatched customer_id)
Inconsistent formatting (extra spaces)
# Phase 2 – Data Cleaning
Steps:
Handled null values using fillna()
Trimmed and standardized string columns
Removed or corrected negative price values
Filtered invalid records
# Phase 3 – Data Validation
Techniques Used:
Anti Joins to detect invalid foreign key relationships
Identified:
Sales with no matching customers
Sales with no valid cars
Validation Report:
Count of invalid records
Summary of cleaned vs rejected data
# Phase 4 – Data Transformation
Key Metrics Generated:
Revenue per Customer
Total amount spent by each customer
Cars per Brand
Count of cars sold per brand
City-wise Revenue
Total sales grouped by city
# Phase 5 – SQL Analysis
Business Insights:
Top 3 Customers per City
Identified using window functions
Repeat Customers
Customers with more than one purchase
Monthly Sales Trend
Aggregated revenue over time
# Phase 6 – Output
Final processed data saved to:
/tmp/car_sales_output
# Key Learnings
End-to-end data pipeline development
Data cleaning and quality checks in PySpark
Handling real-world data issues (nulls, invalid keys)
Using joins and window functions effectively
Writing analytical SQL queries for business insights
# Conclusion

This project demonstrates a complete data engineering workflow, from raw data ingestion to generating actionable insights using PySpark and SQL. It highlights the importance of data quality, validation, and structured transformations in building reliable data pipelines.