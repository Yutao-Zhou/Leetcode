# Write your MySQL query statement below
#### CASE ####
# SELECT
#     employee_id,
#     (CASE
#         WHEN
#             employee_id % 2 = 1
#             AND
#                 name NOT LIKE "M%"
#         THEN
#             salary
#         ELSE
#             0
#     END) AS bonus
# FROM
#     Employees
# ORDER BY
#     employee_id;

#### IF ####
# SELECT
#     employee_id,
#     IF(employee_id % 2 AND name not like "M%", salary, 0) AS bonus
# FROM
#     Employees
# ORDER BY
#     employee_id;

#### * ####
SELECT
    employee_id,
    salary * (employee_id % 2) * (name NOT LIKE "M%") AS bonus
FROM
    Employees
ORDER BY
    employee_id;