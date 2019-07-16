Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+


# Write your MySQL query statement below
SELECT Salary AS SecondHighestSalary
FROM Employee
UNION
SELECT NULL AS SecondHighestSalary
ORDER BY SecondHighestSalary DESC
LIMIT 1 offset 1
