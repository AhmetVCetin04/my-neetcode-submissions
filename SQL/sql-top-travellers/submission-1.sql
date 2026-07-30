-- Write your query below
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM users as u LEFT JOIN rides as r ON u.id = r.user_id
GROUP BY r.user_id, u.name
ORDER BY COALESCE(SUM(r.distance), 0) DESC, u.name ASC;