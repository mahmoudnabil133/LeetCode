# Write your MySQL query statement below
SELECT customer_id , count(*) as count_no_trans
FROM Visits
WHERE Visits.visit_id not in (select visit_id from Transactions)
GROUP BY customer_id
