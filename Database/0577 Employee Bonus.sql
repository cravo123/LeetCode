/* Write your T-SQL query statement below */

-- Solution 1, use ISNULL
-- Notice LEFT JOIN as Bonus table might miss some empId
SELECT
    Employee.name,
    Bonus.bonus
FROM 
    Employee LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE
    ISNULL(Bonus.bonus, 0) < 1000

-- Solution 2, using OR
SELECT
    Employee.name,
    Bonus.bonus
FROM 
    Employee LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE
    Bonus.bonus < 1000
    OR Bonus.bonus IS NULL
