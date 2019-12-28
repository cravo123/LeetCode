/* Write your T-SQL query statement below */

-- Solution 1, notice the int and float data type change
-- MSSQL will implicitly change varchar to int when do calculation
SELECT
    country_name,
    CASE
        WHEN AVG(weather_state * 1.0) <= 15 THEN 'Cold'
        WHEN AVG(weather_state * 1.0) >= 25 THEN 'Hot'
        ELSE 'Warm'
    END AS weather_type
FROM
    Countries AS C
    JOIN Weather AS W
        ON C.country_id = W.country_id
        AND W.day BETWEEN '20191101' AND '20191130'
    GROUP BY
        country_name