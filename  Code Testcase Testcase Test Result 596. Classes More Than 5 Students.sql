# Write your MySQL query statement below
SELECT class
FROM Courses C
GROUP BY (C.class)
Having count(class) >= 5
