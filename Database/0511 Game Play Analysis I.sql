/* Write your T-SQL query statement below */

-- GROUP BY and MIN function
SELECT
    player_id, 
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id