from flask_login import UserMixin
from datetime import datetime
from app import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Projetos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    protocol = db.Column(db.String(100), default='http://')
    url = db.Column(db.String(100), unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
