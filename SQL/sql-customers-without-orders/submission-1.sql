-- Write your query below
SELECT c.name
FROM customers AS c LEFT JOIN orders AS o ON c.id = o.customer_id
-- Types of joins, inner means on condition, left means add back left rows
WHERE o.id is NULL