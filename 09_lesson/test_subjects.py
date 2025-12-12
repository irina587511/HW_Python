from models import Subject


def test_create_subject(db_session):
    subject = Subject(name="Математика", teacher="Иванов И.И.")
    db_session.add(subject)
    db_session.commit()

    saved = db_session.query(Subject).filter_by(name="Математика").first()
    assert saved is not None
    assert saved.teacher == "Иванов И.И."


def test_update_subject(db_session):
    subject = Subject(name="Физика", teacher="Петров П.П.")
    db_session.add(subject)
    db_session.commit()
    subject_id = subject.id

    subject.teacher = "Сидоров С.С."
    db_session.commit()

    updated = db_session.query(Subject).get(subject_id)
    assert updated.teacher == "Сидоров С.С."


def test_delete_subject(db_session):
    subject = Subject(name="Химия", teacher="Козлова К.К.")
    db_session.add(subject)
    db_session.commit()

    db_session.delete(subject)
    db_session.commit()

    remaining = db_session.query(Subject).filter_by(name="Химия").first()
    assert remaining is None
