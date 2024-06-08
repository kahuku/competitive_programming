# Write your MySQL query statement below
SELECT t.num AS 'ConsecutiveNums'
FROM (
    SELECT DISTINCT A.num
    FROM Logs A
    LEFT JOIN Logs B ON A.id = B.id-1
    LEFT JOIN Logs C ON A.id = C.id-2
    WHERE A.num = B.num AND A.num = C.num
) t;