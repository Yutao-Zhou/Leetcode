# Write your MySQL query statement below
#### dense_rank() ####
# SELECT d.name AS Department, ranked_e.name AS Employee, ranked_e.salary AS Salary
# FROM Department d
# LEFT JOIN 
# (SELECT *, DENSE_RANK() OVER (PARTITION BY
#                      e.departmentId
#                  ORDER BY
#                      e.salary DESC
#                 ) AS "rank" 
# FROM Employee e) ranked_e
# ON ranked_e.departmentId = d.id
# WHERE ranked_e.rank <= 3;

#### nested query ####
SELECT d.name AS Department, r.name AS Employee, r.salary AS Salary
FROM Department d
JOIN(
SELECT *
FROM Employee e1
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary
        AND e2.departmentId = e1.departmentId
)) r
ON d.id = r.departmentId;