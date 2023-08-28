# Write your MySQL query statement below
SELECT requester_id AS id, COUNT(requester_id) AS num
FROM
(SELECT requester_id
FROM RequestAccepted
UNION ALL
SELECT accepter_id
FROM RequestAccepted) g
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1;