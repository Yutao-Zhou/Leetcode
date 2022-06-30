# Write your MySQL query statement below
#### AND ####
# SELECT
#     Users.user_id AS buyer_id,
#     Users.join_date,
#     IFNULL(COUNT(Orders.buyer_id), 0) AS orders_in_2019
# FROM
#     Users
# LEFT JOIN
#     Orders
# ON Users.user_id = Orders.buyer_id
# AND
#     YEAR(order_date) = 2019
# GROUP BY
#     Users.user_id;

#### CASE ####
SELECT
    Users.user_id AS buyer_id,
    Users.join_date,
    SUM(CASE
            WHEN
                YEAR(Orders.order_date) = 2019
            THEN
                1
            ELSE
                0
        END) AS orders_in_2019
FROM
    (Users
    LEFT JOIN
        Orders
    ON Users.user_id = Orders.buyer_id)
GROUP BY
    Users.user_id;