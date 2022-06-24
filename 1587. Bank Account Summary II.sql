# Write your MySQL query statement below
SELECT
    Users.name, SUM(Transactions.amount) as balance
FROM
    Transactions
JOIN
    Users
ON
    Users.account = Transactions.account
GROUP BY
    Users.account
HAVING
    balance > 10000;