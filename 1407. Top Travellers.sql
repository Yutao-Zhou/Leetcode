# Write your MySQL query statement below
SELECT
    Users.name AS name, 
    IFNULL(SUM(distance), 0) AS travelled_distance 
FROM
    Rides
RIGHT JOIN
    Users
ON
    Users.id = Rides.user_id
GROUP BY
    user_id
ORDER BY
    travelled_distance DESC, name ASC;