# Write your MySQL query statement below
#### IN ####
# SELECT name
# FROM Employee
# WHERE id IN
# (SELECT managerId
# FROM Employee
# GROUP BY managerId
# HAVING COUNT(managerId) >= 5)

#### JOIN ####
SELECT name
FROM Employee e
JOIN
(SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(managerId) >= 5) mgr
ON mgr.managerId = e.id