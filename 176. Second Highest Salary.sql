# Write your MySQL query statement below

#### double select ####
# SELECT
#     (SELECT DISTINCT
#         salary
#     FROM
#         Employee
#     ORDER BY
#         salary DESC
#     LIMIT 1,1) AS SecondHighestSalary;

#### MAX and Compare ####
SELECT
    MAX(Salary) AS SecondHighestSalary 
FROM
    Employee
WHERE
    Salary < (SELECT
                    MAX(Salary)
              FROM
                    Employee)