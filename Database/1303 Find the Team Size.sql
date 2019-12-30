/* Write your T-SQL query statement below */

-- Solution 1, use WITH statement
With Team AS (
    SELECT
        team_id,
        COUNT(*) AS team_size
    FROM
        Employee
    GROUP BY
        team_id
)

SELECT
    employee_id,
    team_size
FROM
    Employee
    JOIN Team
    ON
        Employee.team_id = Team.team_id