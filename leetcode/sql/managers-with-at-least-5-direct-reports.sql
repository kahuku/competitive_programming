# Write your MySQL query statement below
SELECT man.name
FROM Employee man
JOIN Employee emp ON emp.managerId = man.id
GROUP BY man.id
HAVING COUNT(emp.id) >= 5;