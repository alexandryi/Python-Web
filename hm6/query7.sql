SELECT s.full_name, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.group_id = 1 AND g.subject_id = 1;
