# Write your MySQL query statement below
# case
# WITH r AS (SELECT user_id,
# SUM(CASE
#   WHEN action = "confirmed" THEN 1
#   ELSE 0
# END) / COUNT(user_id) AS confirmation_rate
# FROM Confirmations
# GROUP BY user_id),
# a AS (SELECT user_id
# FROM Signups)
# SELECT a.user_id, ROUND(IFNULL(confirmation_rate, 0), 2) AS confirmation_rate
# FROM r
# RIGHT JOIN a
# ON a.user_id = r.user_id

# shorter
WITH r AS (SELECT user_id,
AVG(IF(action = "confirmed", 1, 0)) AS confirmation_rate
FROM Confirmations
GROUP BY user_id),
a AS (SELECT user_id
FROM Signups)
SELECT a.user_id, ROUND(IFNULL(confirmation_rate, 0), 2) AS confirmation_rate
FROM r
RIGHT JOIN a
ON a.user_id = r.user_id