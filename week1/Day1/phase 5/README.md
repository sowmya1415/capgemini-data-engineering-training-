## Phase5- Advanced Analytics & Reporting (PySpark / SQL)

## Objective

• The objective of this phase is to perform advanced analytics on the dataset using window functions, aggregations, and segmentation techniques.
• The goal is to generate business insights and final reporting tables.

## Problem Summary

We worked with multiple datasets such as:
customers
orders
order_items
products

The tasks included:

 • Performing advanced analytics using window functions
 • Calculating running totals and rankings
 • Segmenting customers based on spending
 • Creating a final reporting dataset

## Approach

• Loaded all datasets into PySpark DataFrames
• Performed data cleaning:
• Handled null values
• Converted data types (e.g., price to double)
• Joined tables using keys like:
• customer_id
• order_id

Applied advanced transformations:

• Window functions (RANK, DENSE_RANK)
• Aggregations (SUM, COUNT)

Created final reporting dataset

• Key Concepts Used
• Window Functions

Used for ranking and running totals

Examples:

RANK() → Top customers per city
DENSE_RANK() → Top products
Running total using SUM() OVER

• Aggregations
SUM() → Total sales
COUNT() → Total orders

• Customer Segmentation
Gold → High spenders (>10000)
Silver → Medium (5000–10000)
Bronze → Low (<5000)

## Output / Results:

The following outputs were generated:
• Top 3 customers per city
• Daily sales with running total
• Top products based on sales
• Customer lifetime value (CLV)
• Customer segmentation
• Final reporting table

## Final Reporting Table Includes:
-> customer_id
-> customer_city
-> total_spend
-> segment
-> total_orders

## uses

• Business decision making
• Customer targeting
• Sales analysis

## Data Engineering Considerations
• Ensured correct joins to avoid duplicates
• Handled data type issues (string → numeric)
• Validated results using sample outputs
• Used window functions efficiently

## Challenges Faced
• Understanding window functions
• Handling large joins
• Fixing data type issues
• Managing SQL vs PySpark differences

## Learnings
• How to use window functions in real scenarios
• Importance of data validation
• Difference between aggregation and window functions
• Building end-to-end data pipelines

## Files
• solution.py → PySpark implementation
• sql_queries.sql → SQL version
• outputs/ → Screenshots of result
