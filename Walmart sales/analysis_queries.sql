-- Walmart Sales Analysis: reusable MySQL 8 queries
-- Load Walmart sales database first:
-- mysql -u root -p < "Walmart sales/walmartsales_backup.sql"
USE walmartsales;

-- 1. Overall business KPIs
SELECT
    COUNT(*) AS invoice_count,
    SUM(quantity) AS units_sold,
    ROUND(SUM(total), 2) AS total_sales,
    ROUND(SUM(cogs), 2) AS cost_of_goods_sold,
    ROUND(SUM(gross_income), 2) AS gross_income,
    ROUND(AVG(rating), 2) AS average_rating
FROM sales;

-- 2. Sales and gross income by branch and city
SELECT branch, city,
       COUNT(*) AS invoices,
       ROUND(SUM(total), 2) AS sales,
       ROUND(SUM(gross_income), 2) AS gross_income
FROM sales
GROUP BY branch, city
ORDER BY sales DESC;

-- 3. Product-line performance
SELECT product_line,
       SUM(quantity) AS units_sold,
       ROUND(SUM(total), 2) AS sales,
       ROUND(AVG(rating), 2) AS average_rating
FROM sales
GROUP BY product_line
ORDER BY sales DESC;

-- 4. Month-wise sales trend
SELECT month_name,
       ROUND(SUM(total), 2) AS monthly_sales
FROM sales
GROUP BY month_name
ORDER BY MIN(date);

-- 5. Payment-method distribution
SELECT payment,
       COUNT(*) AS invoice_count,
       ROUND(SUM(total), 2) AS sales
FROM sales
GROUP BY payment
ORDER BY sales DESC;

-- 6. Member versus normal customers
SELECT customer_type,
       COUNT(*) AS invoice_count,
       SUM(quantity) AS units_sold,
       ROUND(SUM(total), 2) AS sales,
       ROUND(AVG(total), 2) AS average_invoice_value
FROM sales
GROUP BY customer_type
ORDER BY sales DESC;

-- 7. Sales by gender
SELECT gender,
       COUNT(*) AS invoice_count,
       ROUND(SUM(total), 2) AS sales,
       ROUND(AVG(rating), 2) AS average_rating
FROM sales
GROUP BY gender;

-- 8. Day-of-week performance
SELECT day_name,
       COUNT(*) AS invoice_count,
       ROUND(SUM(total), 2) AS sales
FROM sales
GROUP BY day_name
ORDER BY FIELD(day_name,
    'Monday','Tuesday','Wednesday','Thursday',
    'Friday','Saturday','Sunday');

-- 9. Sales by time of day
SELECT time_of_day,
       COUNT(*) AS invoice_count,
       ROUND(SUM(total), 2) AS sales,
       ROUND(AVG(total), 2) AS average_invoice_value
FROM sales
GROUP BY time_of_day
ORDER BY sales DESC;

-- 10. Rating by product line
SELECT product_line,
       ROUND(AVG(rating), 2) AS average_rating,
       COUNT(rating) AS rated_invoices
FROM sales
GROUP BY product_line
ORDER BY average_rating DESC;

-- 11. Ten highest-value invoices
SELECT invoice_id, date, branch, city, product_line,
       quantity, total, payment, rating
FROM sales
ORDER BY total DESC
LIMIT 10;

-- 12. Rank product lines by total sales (MySQL 8+)
SELECT product_line, sales,
       DENSE_RANK() OVER (ORDER BY sales DESC) AS sales_rank
FROM (
    SELECT product_line, SUM(total) AS sales
    FROM sales
    GROUP BY product_line
) AS product_summary;

-- 13. Compare each month with the previous month (MySQL 8+)
WITH monthly_sales AS (
    SELECT MIN(date) AS month_start,
           month_name,
           SUM(total) AS sales
    FROM sales
    GROUP BY month_name
),
month_comparison AS (
    SELECT month_name, month_start, sales,
           LAG(sales) OVER (ORDER BY month_start) AS previous_month_sales
    FROM monthly_sales
)
SELECT month_name,
       ROUND(sales, 2) AS sales,
       ROUND(previous_month_sales, 2) AS previous_month_sales,
       ROUND(sales - previous_month_sales, 2) AS sales_change
FROM month_comparison
ORDER BY month_start;

-- 14. Daily sales with a running total (MySQL 8+)
WITH daily_sales AS (
    SELECT DATE(date) AS sales_date, SUM(total) AS sales
    FROM sales
    GROUP BY DATE(date)
)
SELECT sales_date,
       ROUND(sales, 2) AS daily_sales,
       ROUND(SUM(sales) OVER (ORDER BY sales_date), 2) AS running_sales
FROM daily_sales
ORDER BY sales_date;

-- 15. Product-line sales by city
SELECT city, product_line,
       ROUND(SUM(total), 2) AS sales
FROM sales
GROUP BY city, product_line
ORDER BY city, sales DESC;

-- 16. Branch performance by time of day
SELECT branch, time_of_day,
       COUNT(*) AS invoice_count,
       ROUND(SUM(total), 2) AS sales
FROM sales
GROUP BY branch, time_of_day
ORDER BY branch, sales DESC;

-- 17. Product lines with sales above the average product-line sales
WITH product_sales AS (
    SELECT product_line, SUM(total) AS sales
    FROM sales
    GROUP BY product_line
)
SELECT product_line, ROUND(sales, 2) AS sales
FROM product_sales
WHERE sales > (SELECT AVG(sales) FROM product_sales)
ORDER BY sales DESC;

-- 18. Gross-income contribution by product line
SELECT product_line,
       ROUND(SUM(gross_income), 2) AS gross_income,
       ROUND(
           100 * SUM(gross_income) / NULLIF((SELECT SUM(gross_income) FROM sales), 0),
           2
       ) AS gross_income_share_pct
FROM sales
GROUP BY product_line
ORDER BY gross_income DESC;

-- 19. Rank cities within each branch by sales (MySQL 8+)
WITH city_sales AS (
    SELECT branch, city, SUM(total) AS sales
    FROM sales
    GROUP BY branch, city
)
SELECT branch, city,
       ROUND(sales, 2) AS sales,
       DENSE_RANK() OVER (PARTITION BY branch ORDER BY sales DESC) AS city_rank
FROM city_sales
ORDER BY branch, city_rank;

-- 20. Transaction counts and average value by customer and payment type
SELECT customer_type, payment,
       COUNT(*) AS invoice_count,
       ROUND(AVG(total), 2) AS average_invoice_value,
       ROUND(SUM(total), 2) AS sales
FROM sales
GROUP BY customer_type, payment
ORDER BY customer_type, sales DESC;
