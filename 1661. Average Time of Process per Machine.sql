# Write your MySQL query statement below
#### Naive JOIN Subquery ####
# SELECT e.machine_id, ROUND(AVG(end_time - start_time), 3) AS processing_time
# FROM
# ((SELECT machine_id, process_id, timeStamp AS 'end_time'
# FROM Activity
# WHERE activity_type = "end") e
# JOIN
# (SELECT machine_id, process_id, timeStamp AS 'start_time'
# FROM Activity
# WHERE activity_type = "Start") s
# ON e.machine_id = s.machine_id
#   AND e.process_id = s.Process_id)
# GROUP BY machine_id

#### SELF JOIN ####
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity a1
JOIN Activity a2
ON a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
  AND a1.timestamp < a2.timestamp
GROUP BY a1.machine_id