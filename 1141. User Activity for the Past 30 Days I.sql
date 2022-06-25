# Write your MySQL query statement below
SELECT
    activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users
FROM
    Activity
GROUP BY
    activity_date
HAVING
        MIN(DATE(activity_date)) > '2019-06-27'
    AND
        MAX(DATE(activity_date)) < '2019-07-27';