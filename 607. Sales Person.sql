# Write your MySQL query statement below
#### NOT IN ####
# SELECT
#     name
# FROM
#     SalesPerson
# WHERE
#     sales_id
#     NOT IN
#         (SELECT
#             sales_id 
#         FROM
#             Orders
#         WHERE
#             com_id = (SELECT
#                             com_id
#                       FROM
#                         Company
#                       WHERE
#                         name = "RED"));

#### LEFT JOIN and NOT IN ####
SELECT
    salesperson.name
FROM
    salesperson
WHERE
    salesperson.sales_id
    NOT IN
        (SELECT
            orders.sales_id
        FROM
            orders
                LEFT JOIN
            company ON orders.com_id = company.com_id
        WHERE
            company.name = 'RED')