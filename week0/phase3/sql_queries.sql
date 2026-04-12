#Daily Sales
SELECT sale_date,
       SUM(total_amount) AS total_sales,
       COUNT(*) AS num_orders
FROM sales
WHERE total_amount > 0
GROUP BY sale_date
ORDER BY sale_date;

# City-wise Revenue
SELECT c.city,
       SUM(s.total_amount) AS city_total_revenue
FROM sales s
JOIN customers c
  ON s.customer_id = c.customer_id
WHERE s.total_amount > 0
  AND c.city IS NOT NULL
GROUP BY c.city
ORDER BY c.city;

#Customers more than 2

SELECT customer_id,
       COUNT(*) AS order_count
FROM sales
WHERE total_amount > 0
GROUP BY customer_id
HAVING COUNT(*) > 2
ORDER BY order_count DESC;

# Highest Spending Customer per City
WITH customer_spend AS (
    SELECT s.customer_id,
           c.city,
           SUM(s.total_amount) AS total_spend
    FROM sales s
    JOIN customers c
      ON s.customer_id = c.customer_id
    WHERE s.total_amount > 0
    GROUP BY s.customer_id, c.city
)
SELECT customer_id, city, total_spend
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY city ORDER BY total_spend DESC) AS rank
    FROM customer_spend
) t
WHERE rank = 1
ORDER BY city;

# Final Report
SELECT s.customer_id,
       c.city,
       SUM(s.total_amount) AS total_spend,
       COUNT(*) AS order_count
FROM sales s
JOIN customers c
  ON s.customer_id = c.customer_id
WHERE s.total_amount > 0
  AND c.city IS NOT NULL
GROUP BY s.customer_id, c.city
ORDER BY s.customer_id;
