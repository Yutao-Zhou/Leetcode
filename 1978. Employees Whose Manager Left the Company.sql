# Write your MySQL query statement below
#### Self Join ####
# SELECT e.employee_id
#   FROM Employees e
#   LEFT JOIN Employees m
#   ON e.manager_id = m.employee_id
#   WHERE e.salary < 30000
#     AND e.manager_id IS NOT NULL
#     AND m.employee_id IS NULL
#   ORDER BY employee_id

#### NOT IN ####
SELECT employee_id
  FROM Employees
  WHERE salary < 30000
    AND manager_id NOT IN (SELECT employee_id FROM Employees)
  ORDER BY employee_id