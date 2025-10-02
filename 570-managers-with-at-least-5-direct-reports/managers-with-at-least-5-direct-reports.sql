SELECT m.name
FROM Employee e
JOIN Employee m
  ON e.managerId = m.id   -- e = employee, m = manager
GROUP BY m.id, m.name
HAVING COUNT(e.id) >= 5;