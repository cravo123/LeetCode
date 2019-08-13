/* Write your T-SQL query statement below */
SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM
    Sales
GROUP BY product_id