SELECT 
  t1.id,
  CASE 
    WHEN MAX(t1.p_id) IS NULL THEN 'Root'
    WHEN COUNT(t2.id) > 0 THEN 'Inner'
    ELSE 'Leaf'
  END AS type
FROM Tree t1
LEFT JOIN Tree t2
  ON t1.id = t2.p_id
GROUP BY t1.id;


