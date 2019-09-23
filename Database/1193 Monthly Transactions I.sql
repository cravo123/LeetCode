# Write your MySQL query statement below
-- Solution 1, CASE WHEN and CAST function
SELECT
    CONCAT(CAST(YEAR(trans_date) AS CHAR(4)), '-', LPAD(CAST(MONTH(trans_date) AS CHAR), 2, '0')) AS month,
    country,
    COUNT(1) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count, 
    SUM(amount) as trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM transactions
GROUP BY month, country