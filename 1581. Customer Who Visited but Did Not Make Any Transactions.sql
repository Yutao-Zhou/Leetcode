# Write your MySQL query statement below

#### LEFT JOIN ####
# SELECT 
#     COUNT(Visits.visit_id) AS count_no_trans,
#     customer_id
# FROM
#     Visits
# LEFT JOIN Transactions
#     ON Visits.visit_id = Transactions.visit_id
# WHERE
#     Transactions.visit_id is Null
# GROUP BY customer_id;

#### NOT IN ####
SELECT
    customer_id,
    COUNT(*) as count_no_trans
FROM
    Visits
WHERE
    visit_id 
    NOT IN (
        SELECT 
            DISTINCT visit_id 
        FROM
            Transactions)
GROUP BY customer_id;