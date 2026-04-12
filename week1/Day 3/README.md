# DAY-3: SQL Practice – Window Functions, CASE WHEN & Regex

##  Overview

Today, I focused on strengthening my SQL skills by practicing key concepts that are widely used in data analysis and data engineering:

* Window Functions
* CASE WHEN Statements
* Regular Expressions (Regex)

This practice helped me understand how to perform advanced data transformations, conditional logic, and pattern-based data extraction.

---

## Topics Covered

# 1. Window Functions

Window functions allow performing calculations across a set of rows related to the current row without collapsing the result set.

#### Key Functions Practiced:

* `ROW_NUMBER()`
* `RANK()` and `DENSE_RANK()`
* `SUM() OVER()`
* `COUNT() OVER()`
* `PARTITION BY`
* `ORDER BY` within window functions

#### Example:

```sql
SELECT 
  employee_id,
  department,
  salary,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_in_dept
FROM employees;
```
 **Use Case:** Ranking employees within each department.

---

# 2. CASE WHEN Statements

Used to apply conditional logic in SQL queries, similar to `if-else` conditions in programming.

#### Syntax:

```sql
CASE 
  WHEN condition THEN result
  ELSE result
END
```

#### Example:

```sql
SELECT 
  employee_id,
  salary,
  CASE 
    WHEN salary > 50000 THEN 'High'
    WHEN salary BETWEEN 30000 AND 50000 THEN 'Medium'
    ELSE 'Low'
  END AS salary_category
FROM employees;
```
# 3. Regular Expressions (Regex)

Regex is used to extract, filter, and validate string patterns.

#### Concepts Practiced:

* Extracting numbers from strings
* Extracting text before/after symbols (`@`, `.`, `_`)
* Pattern matching using anchors (`^`, `$`)
* Character classes (`[0-9]`, `[A-Za-z]`)
* Quantifiers (`+`, `{n}`)

#### Example:

```sql
SELECT 
  email,
  REGEXP_SUBSTR(email, '^[^@]+') AS username
FROM users;
```

# Skills Gained

* Writing efficient SQL queries for real-world datasets
* Applying window functions for ranking and aggregation
* Using CASE WHEN for dynamic transformations
* Leveraging regex for complex string manipulation

---

# Key Learnings

* Window functions do not reduce rows like `GROUP BY`
* CASE WHEN improves query readability and flexibility
* Regex is powerful for data cleaning and parsing tasks
* Combining these concepts enables advanced data processing

---

# Conclusion

This practice session enhanced my ability to handle complex SQL scenarios involving ranking, conditional logic, and string manipulation. These skills are essential for roles in data engineering and analytics.
