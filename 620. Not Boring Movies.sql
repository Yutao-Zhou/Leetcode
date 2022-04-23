# Write your MySQL query statement below
#### simple quary ####
# SELECT *
# FROM Cinema
# WHERE description != "boring"
# and mod(id, 2) = 1
# ORDER BY rating DESC

#### NOT LIKE ####
SELECT *
FROM Cinema
WHERE mod(id, 2) = 1
and description NOT LIKE "boring"
ORDER BY rating DESC