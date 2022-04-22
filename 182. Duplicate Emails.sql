# Write your MySQL query statement below
#### count frequency ####
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1