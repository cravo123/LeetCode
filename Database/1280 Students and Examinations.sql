/* Write your T-SQL query statement below */

-- Solution 1, WITH statement
WITH num AS (
    SELECT
        student_id,
        subject_name,
        COUNT(student_id) AS cnt
    FROM
        Examinations
    GROUP BY
        student_id,
        subject_name
),

Info AS (
    SELECT 
        S.student_id, 
        S.student_name, 
        T.subject_name
    FROM 
        Students AS S
        CROSS JOIN Subjects AS T
)

SELECT
    Info.student_id,
    Info.student_name,
    Info.subject_name,
    ISNULL(num.cnt, 0) AS attended_exams
From
    Info
LEFT JOIN num
    ON Info.student_id = num.student_id
    AND Info.subject_name = num.subject_name
ORDER BY
    Info.student_id,
    Info.subject_name