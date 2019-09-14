/* Write your T-SQL query statement below */

-- Solution 1, LEFT JOIN
SELECT
    FirstName, 
    LastName, 
    City, 
    State
FROM
    Person LEFT JOIN Address ON Person.PersonId = Address.PersonId