# Write your MySQL query statement below
DELETE P1 FROM Person p1, Person p2
WHERE P1.email = P2.email and P1.id > P2.id
