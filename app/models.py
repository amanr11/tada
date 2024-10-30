from . import db
from datetime import datetime

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    module_code = db.Column(db.String(10), nullable=False)
    deadline_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Assessment {self.title}>'
