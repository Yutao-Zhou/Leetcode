# Write your MySQL query statement below
SELECT a.student_id, a.student_name, a.subject_name, IFNULL(COUNT(e.student_id), 0) AS attended_exams
FROM
((SELECT *
FROM Students std
CROSS JOIN Subjects sub) a
LEFT JOIN Examinations e
ON a.student_id = e.student_id
AND a.subject_name = e.subject_name)
GROUP BY student_id, student_name, subject_name
ORDER BY student_id, subject_name