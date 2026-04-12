# Phase 4 – Mini Project: Business Pipeline & Analytics

##  Objective

This phase focuses on building a complete end-to-end data pipeline using PySpark. It involves data ingestion, cleaning, transformation, and applying business logic to generate meaningful insights.


## Problem Statement (Summary)

• Perform data cleaning (remove nulls, duplicates, invalid values)
• Calculate daily sales from transaction data
• Generate city-wise revenue using joins
• Identify top customers based on total spend
• Find repeat customers based on order count
• Apply customer segmentation (Gold, Silver, Bronze)
• Build a final reporting table combining all insights

##  Dataset Used

• Dataset: Sample datasets from Spark Playground
• Source: Spark Playground tutorials
• Tables used: customers, sales

##  Approach

1. Loaded datasets from `/samples/` into PySpark DataFrames
2. Cleaned data by removing null keys and duplicate records
3. Converted data types (e.g., total_amount to integer)
4. Filtered invalid values such as negative amounts
5. Performed joins between customers and sales datasets
6. Applied aggregations to calculate metrics like revenue and counts
7. Implemented business logic for customer segmentation
8. Created a final reporting table combining all insights


##  Key Transformations

• `dropna()` and `dropDuplicates()` for data cleaning
• `filter()` for removing invalid data
• `groupBy()` with aggregations (`sum()`, `count()`)
• `join()` for combining datasets
• `when()` for conditional logic (segmentation)
• `orderBy()` and `limit()` for ranking customers


##  Output / Results

• Daily sales report (date, total_sales)
• City-wise revenue (city, total_revenue)
• Top 5 customers based on total spend
• Repeat customers with order count
• Customer segmentation (Gold, Silver, Bronze)
• Final reporting table with customer insights


##  Challenges Faced

• File write permission issues in restricted environment
• Handling missing and inconsistent data
• Implementing segmentation logic correctly
• Combining multiple transformations into a single pipeline

## Learnings

• Building an end-to-end ETL pipeline
• Importance of data cleaning before processing
• Applying business logic using PySpark transformations
• Handling real-world constraints like environment limitations
• Understanding how analytical pipelines are built in practice

## Files in this Folder

• solution.py / notebook → Implementation
• outputs/ → Results 