/* Write your T-SQL query statement below */

-- Solution 1, using CASE and AVG is simpler
SELECT 
    ROUND(100 * AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1.0 ELSE 0.0 END), 2) AS immediate_percentage
FROM delivery

-- Solution 2, WITH statement
-- notice that integer division only returns integer
with A(cnt) AS (
SELECT COUNT(*) FROM delivery WHERE order_date = customer_pref_delivery_date),

B(cnt) AS (
SELECT COUNT(*) FROM delivery)

SELECT ROUND(A.cnt * 100.0 / B.cnt, 2) AS immediate_percentage FROM A, B