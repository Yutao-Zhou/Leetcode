# Write your MySQL query statement below
SELECT product_name, SUM(unit) AS unit
FROM Products p
JOIN Orders o
ON p.product_id = o.product_id
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY p.product_id
HAVING unit >= 100