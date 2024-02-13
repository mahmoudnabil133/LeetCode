# Write your MySQL query statement below
SELECT * FROM Cinema c
WHERE (c.id % 2 != 0) and c.description != 'boring'
ORDER BY c.rating DESC;
