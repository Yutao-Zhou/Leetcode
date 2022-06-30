# Write your MySQL query statement below
#### JOIN ####
# SELECT
#     E.name AS Employee
# FROM
#     Employee AS E
# INNER JOIN
#     Employee AS M
# ON
#     E.managerId = M.id
# WHERE
#     M.salary < E.salary;

#### WHERE ####
SELECT
    e.name AS Employee 
FROM
    Employee AS e,
    Employee AS m
WHERE
    e.managerID = m.id
    AND
        e.salary > m.salary;