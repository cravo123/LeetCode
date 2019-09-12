/* Write your T-SQL query statement below */

-- INNER JOIN
SELECT 
    product_name, 
    year, 
    price
FROM 
    Product INNER JOIN Sales ON Sales.product_id = Product.product_id