import sqlite3
from faker import Faker
import random

fake = Faker()

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

with open('db.sql', 'r') as f:
    cursor.executescript(f.read())

groups = ['Group A', 'Group B', 'Group C']
for g in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (g,))
group_ids = [row[0] for row in cursor.execute("SELECT id FROM groups").fetchall()]

for _ in range(random.randint(3, 5)):
    cursor.execute("INSERT INTO teachers (full_name) VALUES (?)", (fake.name(),))
teacher_ids = [row[0] for row in cursor.execute("SELECT id FROM teachers").fetchall()]

subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'CS', 'Philosophy']
subjects = random.sample(subject_names, random.randint(5, 8))
for s in subjects:
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", 
                   (s, random.choice(teacher_ids)))
subject_ids = [row[0] for row in cursor.execute("SELECT id FROM subjects").fetchall()]

for _ in range(random.randint(30, 50)):
    cursor.execute("INSERT INTO students (full_name, group_id) VALUES (?, ?)",
                   (fake.name(), random.choice(group_ids)))
student_ids = [row[0] for row in cursor.execute("SELECT id FROM students").fetchall()]

for student_id in student_ids:
    for _ in range(random.randint(15, 20)):
        cursor.execute(
            "INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)",
            (
                student_id,
                random.choice(subject_ids),
                random.randint(60, 100),
                fake.date_between(start_date='-1y', end_date='today')
            )
        )

conn.commit()
conn.close()
