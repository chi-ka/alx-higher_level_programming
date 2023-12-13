-- List all cities with their corresponding state names using JOIN
SELECT a.id, a.name, b.name
FROM cities a
JOIN states b
ON a.state_id = b.id
ORDER BY a.id ASC;
