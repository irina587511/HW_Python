from models import Student


def test_create_student(db_session):
    student = Student(name="Иван Иванов", age=20)
    db_session.add(student)
    db_session.commit()

    saved = db_session.query(Student).filter_by(name="Иван Иванов").first()
    assert saved is not None
    assert saved.age == 20


def test_update_student(db_session):
    student = Student(name="Петр Петров", age=22)
    db_session.add(student)
    db_session.commit()
    student_id = student.id

    student.age = 23
    db_session.commit()

    updated = db_session.query(Student).get(student_id)
    assert updated.age == 23


def test_delete_student(db_session):
    student = Student(name="Мария Сидорова", age=19)
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    remaining = db_session.query(Student).filter_by(name="Мария Сидорова").first()
    assert remaining is None
