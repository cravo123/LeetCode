/* Write your T-SQL query statement below */

-- Solution 1, WHERE statement
SELECT
    name,
    population,
    area
FROM
    World
Where
    area > 3e6 OR population > 25e6