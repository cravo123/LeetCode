/* Write your T-SQL query statement below */

-- Solution 1, 
-- neither does NULL equal to an interger nor not equal to an integer
SELECT
    name
FROM
    customer
WHERE referee_id != 2 or referee_id IS NULL