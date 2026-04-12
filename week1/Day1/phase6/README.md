# Phase 6 – Business Pipeline & Advanced Analytics using PySpark

## Objective

In this phase, the goal is to build a complete end-to-end ETL pipeline using PySpark and generate advanced business insights.
This includes data extraction, transformation, segmentation, and final reporting.

## Problem Summary

We were given datasets such as customers and orders.
The tasks were to:
• Clean and prepare the data
• Perform aggregations (daily sales, revenue, etc.)
• Identify top and repeat customers
• Segment customers based on spending behavior
• Generate a final reporting dataset

## Approach
1. Loaded datasets into PySpark DataFrames
2. Performed data cleaning:
   * Removed null values
   * Filtered invalid records (e.g., negative values)
3. Joined datasets using 'customer_id'.
4. Applied transformations:
   * Aggregations (sum, count)
   * Grouping (city-wise, customer-wise)
5. Performed customer segmentation using:
   * Conditional logic (Gold, Silver, Bronze)
   * Quantile-based segmentation
6. Created final reporting table

## Key Transformations Used
• 'join()' → to combine customers and orders
• 'groupBy()' → for aggregations
• 'agg()' → to calculate total sales, revenue
• 'filter()' → to remove invalid data
• 'withColumn()' → to create new columns (segment)
• 'when()' → for conditional segmentation

## Output / Results
The following outputs were generated:
• Daily Sales Report
• City-wise Revenue
• Top Customers
• Repeat Customers
• Customer Segmentation (Gold, Silver, Bronze)
• Final Reporting Table

Outputs can be viewed in the outputs/ folder.

## Data Engineering Considerations

• Ensured data cleaning before analysis
• Handled null and invalid values properly
• Used joins carefully to avoid duplication
• Validated results using counts and sample outputs

## Challenges Faced
• Handling SQL compatibility issues (e.g., unsupported functions like NTILE)
• Debugging column name mismatches
• Managing date format errors
• Implementing quantile segmentation in MySQL

## Learnings
• How to build a complete ETL pipeline using PySpark
• Importance of data cleaning and validation
• Difference between fixed and quantile-based segmentation
• Writing equivalent SQL queries for PySpark logic
• Debugging real-world data issues

## Files in this Folder

• 'solution.py' -> Full PySpark pipeline code
• 'phase6_problem_statement.pdf' -> Problem description
• 'outputs/' -> Output screenshots
• 'README.md' -> Documentation