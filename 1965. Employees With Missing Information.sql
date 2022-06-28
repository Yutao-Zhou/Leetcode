# Write your MySQL query statement below
#### NOT IN ####
# (SELECT
#     employee_id
# FROM
#     Employees
# WHERE
#     employee_id NOT IN (SELECT employee_id FROM Salaries))
# UNION
# (SELECT
#     employee_id
# FROM
#     Salaries
# WHERE
#     employee_id NOT IN (SELECT employee_id FROM Employees))
# ORDER BY
#     employee_id ASC;

#### OUTER JOIN ####
SELECT
    all_employee.employee_id
FROM
    (SELECT
        *
    FROM
        Employees
    LEFT JOIN
        Salaries
    USING
        (employee_id)
    UNION
    SELECT
        *
    FROM
        Employees
    RIGHT JOIN
        Salaries
    USING
        (employee_id))
AS
    all_employee
WHERE
    all_employee.name IS NULL OR all_employee.salary IS NULL
ORDER BY
    all_employee.employee_id ASC;