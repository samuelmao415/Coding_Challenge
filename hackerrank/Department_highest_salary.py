The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest salary in the Sales department.

WITH emp AS
(SELECT DepartmentId, MAX(Salary) AS high_salary
FROM Employee
GROUP BY DepartmentId)
,
emp_tbl AS
(
SELECT e.Name, e.Salary, e.DepartmentId
FROM Employee e
INNER JOIN emp em
ON e.Salary = em.high_salary
AND e.DepartmentId = em.DepartmentId
)
SELECT d.Name AS Department, emp.Name AS Employee, emp.Salary  FROM emp_tbl emp
INNER JOIN Department d
ON d.Id = emp.DepartmentId
