import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PrivilegedAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
