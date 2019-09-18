/* Write your T-SQL query statement below */

-- Solution 1, WHERE filtering
SELECT DISTINCT
    author_id AS id
FROM
    Views
WHERE
    author_id = viewer_id
ORDER BY
    id