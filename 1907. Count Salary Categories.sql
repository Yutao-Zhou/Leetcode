# Write your MySQL query statement below
# Union
# (SELECT "Low Salary" AS category, COUNT(account_id) AS accounts_count
# FROM Accounts
# WHERE income < 20000)
# Union
# (SELECT "Average Salary" AS category, COUNT(account_id) AS accounts_count
# FROM Accounts
# WHERE 20000 <= income  AND income <= 50000)
# Union
# (SELECT "High Salary" AS category, COUNT(account_id) AS accounts_count
# FROM Accounts
# WHERE 50000 < income)

# case
WITH result AS (SELECT
  CASE 
    WHEN income < 20000 THEN "Low Salary"
    WHEN income > 50000 THEN "High Salary"
    ELSE "Average Salary"
  END AS category,
  COUNT(account_id) AS accounts_count
FROM Accounts
GROUP BY category),
Category AS (SELECT "Low Salary" AS category
UNION
SELECT "Average Salary" AS category
UNION
SELECT "High Salary" AS category) 
SELECT Category.category, IFNULL(result.accounts_count, 0) AS accounts_count
FROM result
RIGHT JOIN Category
ON result.category = Category.category