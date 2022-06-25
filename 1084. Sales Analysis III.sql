# Write your MySQL query statement below
SELECT
    Product.product_id, product_name
FROM
    Product
JOIN
(
SELECT
    Sales.product_id
FROM
    Sales
GROUP BY
    Sales.product_id
HAVING
    '2019-01-01' <= MIN(DATE(sale_date))
AND
    MAX(DATE(sale_date)) <= '2019-03-31') AS s
ON Product.product_id = s.product_id;