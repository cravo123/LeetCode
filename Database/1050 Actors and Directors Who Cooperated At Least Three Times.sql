/* Write your T-SQL query statement below */

-- Solution 1, HAVING to filter GROUP BY results

SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING COUNT(*) >= 3