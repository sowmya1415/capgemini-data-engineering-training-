# ETL Pipeline & Data Engineering Workflow

# Objective

This phase focuses on building an end-to-end data pipeline using PySpark by applying ETL (Extract, Transform, Load) concepts. It involves data ingestion, cleaning, transformation, and generating final analytical outputs.

# Problem Statement 
• Read data from multiple file formats (CSV, JSON, Parquet)
• Inspect schema and understand data structure
• Perform data cleaning (nulls, duplicates, invalid values)
• Apply transformations (filtering, aggregation, joins)
• Implement business logic (customer insights, revenue analysis)
• Build a complete ETL pipeline and generate final outputs

# Dataset Used

• Dataset: Sample datasets from Spark Playground
• Source: Spark Playground tutorials
• Tables used: customers, sales

# Approach

1. Loaded datasets into PySpark DataFrames using `/samples/` path
2. Inspected schema using `show()` and `printSchema()`
3. Cleaned data by handling null values and filtering invalid records
4. Converted data types (e.g., string to integer for numeric fields)
5. Joined datasets to combine customer and transaction data
6. Applied aggregations and window functions to generate insights
7. Built final reporting tables as part of ETL pipeline

# Key Transformations

• `dropna()` and `fillna()` for handling missing data
• `filter()` for removing invalid records
• `groupBy()` with aggregations (`sum()`, `count()`)
• `join()` for combining datasets
• Window functions (`rank()`) for ranking logic

# Output

• Daily sales aggregation
• City-wise revenue analysis
• Identification of repeat customers
• Highest spending customer per city
• Final reporting table with customer insights

# Challenges Faced

• File path issues while accessing datasets
• Handling missing and inconsistent data
• Understanding correct schema and column names
• Applying window functions correctly

# Learnings
• Understanding ETL workflow (Extract, Transform, Load)
• Importance of data cleaning before analysis
• Combining multiple transformations into a pipeline
• Applying real-world data engineering concepts using PySpark
