# Write your MySQL query statement below
#### LEFT JOIN AND FILTER ####
# SELECT name, bonus
# FROM Employee e
# LEFT JOIN Bonus b
# ON e.empId = b.empId
# WHERE bonus < 1000 OR bonus IS NULL

#### COALESCE ####
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE COALESCE(bonus, 0) < 1000