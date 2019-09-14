/* Write your T-SQL query statement below */

-- Solution 1, Self JOIN
SELECT
    Worker.Name AS Employee
FROM
    Employee AS Worker
    JOIN Employee AS Manager ON Worker.ManagerId = Manager.Id
WHERE
    Worker.Salary > Manager.Salary