# Write your MySQL query statement below
#### Select and union ####
# SELECT id, "Root" AS type FROM Tree WHERE p_id IS null
# UNION
# SELECT t1.id, "Inner" AS type FROM Tree t1 WHERE EXISTS (SELECT p_id FROM Tree t2 WHERE t2.p_id = t1.id AND t1.p_id IS NOT null)
# UNION
# SELECT t1.id, "Leaf" AS type FROM Tree t1 WHERE (NOT EXISTS (SELECT p_id FROM Tree t2 WHERE t2.p_id = t1.id) AND t1.p_id IS NOT null);

#### Case ####
SELECT id,
(CASE WHEN p_id IS null THEN 'Root'
     WHEN id IN (SELECT p_id FROM tree) THEN 'Inner'
     ELSE 'Leaf' END) AS type
FROM Tree