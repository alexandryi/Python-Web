import random
from datetime import date
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade

fake = Faker()

engine = create_engine('postgresql+psycopg2://postgres:melnyk2006@localhost:5432/university')
Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=f'Group {i+1}') for i in range(3)]
session.add_all(groups)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(random.randint(3,5))]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=fake.word().capitalize(), teacher=random.choice(teachers)) for _ in range(random.randint(5,8))]
session.add_all(subjects)
session.commit()

students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(random.randint(30,50))]
session.add_all(students)
session.commit()

grades = []
for student in students:
    subjects_for_student = random.sample(subjects, k=len(subjects))
    for subject in subjects_for_student:
        for _ in range(random.randint(5, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=round(random.uniform(1, 12), 2),
                date_of=fake.date_between(start_date='-1y', end_date='today')
            )
            grades.append(grade)

session.add_all(grades)
session.commit()

print("Database seeded!")
