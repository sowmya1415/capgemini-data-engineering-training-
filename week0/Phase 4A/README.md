#  Phase 4A – Bucketing & Segmentation in PySpark

##  Objective

This phase focuses on understanding how continuous numerical data can be converted into meaningful categories using bucketing and segmentation techniques. It helps in simplifying analysis and supporting business decision-making.

##  Problem Statement (Summary)

• Convert continuous values (total spend) into categories like Gold, Silver, Bronze
• Implement segmentation using conditional logic
• Group customers based on segments and analyze distribution
• Apply alternative bucketing techniques (quantile-based, window functions)
• Compare different segmentation methods
• Understand the impact of segmentation on business insights


##  Dataset Used

• Dataset: Processed dataset from previous phases (customer spend data)
• Source: Spark Playground / previous ETL pipeline outputs
• Tables used: Customer-level aggregated dataset (customer_id, total_spend, etc.)


##  Approach

1. Used aggregated customer spend data from previous pipeline
2. Applied conditional logic to classify customers into segments (Gold, Silver, Bronze)
3. Grouped data by segment to analyze customer distribution
4. Implemented alternative methods like quantile-based segmentation and window-based ranking
5. Compared results across different segmentation approaches
6. Evaluated which method provides better business insights


##  Key Transformations

• `when()` for conditional segmentation
• `groupBy()` with `count()` for segment distribution
• Window functions (`percent_rank()`) for ranking-based segmentation
• Quantile functions (`approxQuantile`) for dynamic segmentation
• MLlib `Bucketizer` for bucket-based classification

##  Output / Results

• Customer segmentation into Gold, Silver, and Bronze categories
• Distribution of customers across segments
• Comparison of segmentation methods (fixed vs dynamic)
• Insights into customer spending behavior


## Challenges Faced

• Choosing appropriate thresholds for segmentation
• Understanding differences between segmentation techniques
• Interpreting results from different methods
• Deciding which method is suitable for business use cases


##  Learnings

• Importance of converting continuous data into categories
• Differences between fixed-rule segmentation and dynamic bucketing
• Use of quantiles for balanced segmentation
• Application of window functions for ranking-based analysis
• How segmentation helps in business decision-making



##  Files in this Folder

• solution.py / notebook → Implementation
• outputs/ → Results 