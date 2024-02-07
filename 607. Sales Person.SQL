# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson s
WHERE s.sales_id not in (SELECT o.sales_id
                         FROM Orders INNER JOIN Company C
                         ON o.com_id = c.com_id
                         where c.name = 'RED')
