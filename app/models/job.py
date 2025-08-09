from app import db
from datetime import datetime


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pending')
    submission_date = db.Column(db.Date)
    notes = db.Column(db.Text)

    def __init__(self, **kwargs):
        super(Job, self).__init__(**kwargs)
        if not self.status:
            self.status = 'pending'
        if not self.submission_date:
            self.submission_date = datetime.now().date()

    def __repr__(self):
        return f"<Job {self.id} - {self.company_name} - {self.position}>"

    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'position': self.position,
            'status': self.status,
            'submission_date': self.submission_date,
            'notes': self.notes
        }
