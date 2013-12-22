MATCH (n)-[:WORKS_ON]->(m) 
WITH n, COUNT(m) as c
WHERE c > 1
RETURN n
