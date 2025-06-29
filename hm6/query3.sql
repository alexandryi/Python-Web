SELECT gr.name, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
WHERE g.subject_id = 1
GROUP BY gr.id;
