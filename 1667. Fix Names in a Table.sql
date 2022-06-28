# Write your MySQL query statement below
#### CONCAT + SUBSTING ####
# SELECT
#     user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
# FROM
#     Users
# ORDER BY
#     user_id ASC;

#### LEFT and RIGHT ####
SELECT
    user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) - 1))) AS name
FROM
    Users
ORDER BY
    user_id ASC;