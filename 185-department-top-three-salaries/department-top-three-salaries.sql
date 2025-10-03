select
d.name as department,
e.name as employee,
e.salary as Salary
from
(
    select *,
            dense_rank() over(partition by departmentid order by salary desc) as rnk
            from employee
)e
JOIN Department d
ON e.departmentId = d.id
WHERE e.rnk <= 3
ORDER BY Department, Salary DESC;