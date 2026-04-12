## 1. CREATE TABLES

CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    age INT
);

INSERT INTO customers VALUES
(1, 'Ravi', 'Hyderabad', 25),
(2, 'Sita', 'Chennai', 32),
(3, 'Arun', 'Hyderabad', 28),
(4, 'Meena', 'Bengaluru', 35),
(5, 'Kiran', 'Chennai', 22);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    amount INT,
    date DATE
);

INSERT INTO orders VALUES
(101, 1, 2500, '2026-03-01'),
(102, 2, 1800, '2026-03-02'),
(103, 1, 3200, '2026-03-03'),
(104, 3, 1500, '2026-03-04'),
(105, 5, 2800, '2026-03-05');

## 2. TOTAL SPEND PER CUSTOMER

CREATE VIEW total_spend AS
SELECT c.customer_id, c.name,
       SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

## 3. CONDITIONAL SEGMENTATION

CREATE VIEW segment_fixed AS
SELECT *,
       CASE
           WHEN total_spend > 5000 THEN 'Gold'
           WHEN total_spend BETWEEN 2000 AND 5000 THEN 'Silver'
           ELSE 'Bronze'
       END AS segment
FROM total_spend;

## 4. QUANTILE SEGMENTATION (Using NTILE)

CREATE VIEW segment_quantile AS
SELECT *,
       CASE
           WHEN bucket = 1 THEN 'Bronze'
           WHEN bucket = 2 THEN 'Silver'
           ELSE 'Gold'
       END AS segment_quantile
FROM (
    SELECT *,
           NTILE(3) OVER (ORDER BY total_spend) AS bucket
    FROM total_spend
) t;

## 5. SEGMENT COUNT

SELECT segment, COUNT(*) AS count
FROM segment_fixed
GROUP BY segment;

## 6. COMPARISON

SELECT f.name,
       f.total_spend,
       f.segment,
       q.segment_quantile
FROM segment_fixed f
JOIN segment_quantile q
ON f.customer_id = q.customer_id;

## 7. FINAL OUTPUTS

SELECT * FROM segment_fixed;
SELECT * FROM segment_quantile;