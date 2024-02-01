"""
select a dup emails
"""
# Write your MySQL query statement below
SELECT DISTINCT email as Email
from Person p1
where email in (select  email from
                Person p2
                where p1.email = p2.email and p1.id < p2.id)
