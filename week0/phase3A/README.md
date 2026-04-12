# Data Quality & Cleaning Challenge

# Objective

This phase focuses on understanding the importance of data cleaning by working with messy datasets. It involves identifying data quality issues and applying cleaning techniques before performing any analysis.

# Problem Statement 

• Identify data issues such as null values, duplicates, and invalid entries
• Remove rows with missing key values
• Handle missing data using appropriate techniques
• Remove duplicate records
• Filter invalid values (e.g., negative age)
• Validate cleaned data using row counts and perform aggregation

# Dataset Used

• Dataset: Manually created sample dataset with intentional errors
• Source: Spark Playground exercise
• Tables used: Single DataFrame (customer data with nulls, duplicates, invalid values)

# Approach

1. Created a PySpark DataFrame with messy data
2. Identified issues like null values, duplicates, and invalid entries
3. Removed rows with null `customer_id`
4. Filled missing values for non-key columns
5. Removed duplicate records
6. Filtered invalid values 
7. Validated cleaning by comparing row counts before and after
8. Performed aggregation (customers per city)

# Key Transformations

• `dropna()` for removing null key values
• `fillna()` for handling missing data
• `dropDuplicates()` for removing duplicate rows
• `filter()` for removing invalid values
• `groupBy()` with `count()` for aggregation

# Output

• Cleaned dataset with valid and consistent data
• Row count comparison before and after cleaning
• Customer count per city after cleaning

# Challenges Faced

• Identifying all types of data issues in the dataset
• Deciding how to handle missing values appropriately
• Ensuring no important data is lost during cleaning

# Learnings

• Real-world data is often messy and requires preprocessing
• Data cleaning is essential before performing analysis
• Invalid or duplicate data can lead to incorrect results
• Validation is important to ensure data quality
