# Write your MySQL query statement below

#### NOT IN ####
# SELECT
#     name AS Customers
# FROM
#     Customers
# WHERE
#     Customers.id NOT IN
#     (SELECT
#         customerId 
#     FROM
#         Orders);

#### LEFT JOIN ####
SELECT
    name AS Customers
FROM
    Customers
LEFT JOIN
    Orders
ON
    Customers.id = Orders.customerId
WHERE
    Orders.customerId IS NULL;