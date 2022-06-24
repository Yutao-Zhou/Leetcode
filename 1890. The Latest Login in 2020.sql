# Write your MySQL query statement below

#### LIKE ####
# SELECT
#     user_id, MAX(time_stamp) AS last_stamp
# FROM
#     Logins
# WHERE 
#     time_stamp LIKE '2020%'
# GROUP BY
#     user_id;

#### YEAR ####
SELECT
    user_id, MAX(time_stamp) AS last_stamp
FROM
    Logins
WHERE 
    YEAR(time_stamp) = 2020
GROUP BY
    user_id;