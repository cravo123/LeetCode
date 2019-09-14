/* Write your T-SQL query statement below */

-- Solution 1, WHERE to filter
SELECT
    id,
    movie,
    description,
    rating
FROM 
    cinema
WHERE
    description != 'boring'
    AND id % 2 = 1
ORDER BY
    rating DESC