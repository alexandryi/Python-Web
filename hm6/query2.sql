SELECT s.full_name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
