# Write your MySQL query statement below
#### JOIN ####
# SELECT t.request_at AS Day, ROUND((total - IFNULL(completed, 0)) / total, 2) AS 'Cancellation Rate'
# FROM
#   (SELECT COUNT(id) AS completed, request_at
#   FROM Trips
#   WHERE client_id IN 
#       (SELECT users_id
#       FROM Users
#       WHERE banned = 'No')
#     AND driver_id IN 
#       (SELECT users_id
#       FROM Users
#       WHERE banned = 'No')
#     AND status = 'completed'
#   GROUP BY request_at) c
#   RIGHT JOIN
#   (SELECT COUNT(id) AS total, request_at
#   FROM Trips
#   WHERE client_id IN 
#       (SELECT users_id
#       FROM Users
#       WHERE banned = 'No')
#     AND driver_id IN 
#       (SELECT users_id
#       FROM Users
#       WHERE banned = 'No')
#   GROUP BY request_at) t
#   ON c.request_at = t.request_at
# HAVING Day <= '2013-10-03'
#   AND Day >= '2013-10-01'

#### IF ####
SELECT Request_at AS Day, ROUND(SUM(IF(Status = 'completed', 0, 1)) / COUNT(Status), 2) as 'Cancellation Rate' 
FROM Trips 
WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes') 
    AND Driver_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes')
    AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Trips.Request_at