/* Write your T-SQL query statement below */

-- Solution 1, SELF OUTER JOIN
SELECT
    MIN(ABS(A.x - B.x)) AS shortest
FROM
    point AS A FULL OUTER JOIN point AS B ON 1 = 1
WHERE A.x != B.x

-- Solution 1.1, a more elegant implementation
SELECT
    MIN(A.x - B.x) AS shortest
FROM
    point AS A FULL JOIN point AS B ON 1 = 1
WHERE A.x > B.x