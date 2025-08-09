import pytest
from app import create_app
from app.models import db, Job


@pytest.fixture
def app():
    app = create_app({'TESTING': True})
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


def test_job_creation(app):
    with app.app_context():
        job = Job(company_name="Test Corp", position="Developer")
        db.session.add(job)
        db.session.commit()
        assert Job.query.count() == 1
