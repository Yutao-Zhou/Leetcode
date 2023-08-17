# Write your MySQL query statement below
#### get date and join ####
SELECT DISTINCT(p1.product_id), IF (p2.change_date IS NULL, 10, p1.new_price) AS price
FROM Products p1
LEFT JOIN
(SELECT product_id, MAX(change_date) AS change_date
FROM Products
WHERE change_date <= '2019-08-16'
GROUP BY product_id) p2
ON p1.product_id = p2.product_id
WHERE p1.change_date = p2.change_date
  OR p2.change_date IS NULL

#### create two table and union ####
# (SELECT product_id, 10 AS price
# FROM Products
# GROUP BY product_id
# HAVING min(change_date) > '2019-08-16')
# UNION ALL
# (SELECT product_id, new_price AS price
# FROM Products
# WHERE (product_id, change_date) IN 
#   (SELECT product_id, MAX(change_date)
#   FROM Products
#   WHERE change_date <= '2019-08-16'
#   GROUP BY product_id))