from sqlalchemy import func, desc, cast, Numeric
from models import Student, Grade, Subject, Teacher, Group

def select_1(session):
    return session.query(
        Student.fullname,
        func.round(
            cast(func.avg(Grade.grade), Numeric), 2
        ).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(session, subject_id):
    return session.query(
        Student.fullname,
        func.round(
            cast(func.avg(Grade.grade), Numeric), 2
        ).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(session, subject_id):
    return session.query(
        Group.name,
        func.avg(Grade.grade).label('avg_grade')
    ).select_from(Group).join(
        Student, Group.id == Student.group_id
    ).join(
        Grade, Student.id == Grade.student_id
    ).filter(
        Grade.subject_id == subject_id
    ).group_by(Group.id).all()


def select_4(session):
    return session.query(
        func.round(
            cast(func.avg(Grade.grade), Numeric), 2
        ).label('avg_grade')
    ).one()

def select_5(session, teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(session, group_id):
    return session.query(Student.fullname).filter(Student.group_id == group_id).all()

def select_7(session, group_id, subject_id):
    return session.query(
        Student.fullname,
        Grade.grade
    ).join(Grade).filter(
        Student.group_id == group_id,
        Grade.subject_id == subject_id
    ).all()

def select_8(session, teacher_id):
    return session.query(
        func.round(
            cast(func.avg(Grade.grade), Numeric), 2
        ).label('avg_grade')
    ).join(Subject).filter(Subject.teacher_id == teacher_id).one()

def select_9(session, student_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(Grade.student_id == student_id).distinct().all()

def select_10(session, student_id, teacher_id):
    return session.query(
        Subject.name
    ).join(Grade).filter(
        Grade.student_id == student_id,
        Subject.teacher_id == teacher_id
    ).distinct().all()
