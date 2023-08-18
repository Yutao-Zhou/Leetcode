# Write your MySQL query statement below
#### Calculate ####
# SELECT query_name, ROUND(SUM(rating / position) / COUNT(rating), 2) AS quality, ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(rating) * 100, 2) AS poor_query_percentage
# FROM Queries
# GROUP BY query_name

#### AVG ####
SELECT query_name, ROUND(AVG(rating / position) , 2) AS quality, ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name