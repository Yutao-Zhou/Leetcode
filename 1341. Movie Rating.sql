# Write your MySQL query statement below
(SELECT u.name AS results
FROM MovieRating mrp
LEFT JOIN Users u
ON mrp.user_id = u.user_id
GROUP BY mrp.user_id
ORDER BY COUNT(mrp.movie_id) DESC, u.name
LIMIT 1)
UNION ALL
(SELECT m.title AS results
FROM MovieRating mr
LEFT JOIN Movies m
ON mr.movie_id = m.movie_id
WHERE mr.created_at LIKE "2020-02%"
GROUP BY mr.movie_id
ORDER BY AVG(mr.rating) DESC, m.title
LIMIT 1)