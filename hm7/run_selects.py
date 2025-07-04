from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from models import Base

engine = create_engine("postgresql+psycopg2://postgres:melnyk2006@localhost:5432/university")

session = Session(engine)

print("Select 1:", select_1(session))

subject_id = 1
teacher_id = 1
group_id = 1
student_id = 1

print("Select 2:", select_2(session, subject_id))
print("Select 3:", select_3(session, subject_id))
print("Select 4:", select_4(session))
print("Select 5:", select_5(session, teacher_id))
print("Select 6:", select_6(session, group_id))
print("Select 7:", select_7(session, group_id, subject_id))
print("Select 8:", select_8(session, teacher_id))
print("Select 9:", select_9(session, student_id))
print("Select 10:", select_10(session, student_id, teacher_id))
