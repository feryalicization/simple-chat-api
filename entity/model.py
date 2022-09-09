from . import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    begin_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    deleted_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    full_name = db.Column(db.String(225))
    username = db.Column(db.String(225))
    email = db.Column(db.String(225), unique=True)
    notlp = db.Column(db.String(225))
    jenis_kelamin = db.Column(db.String(225))
    avatar = db.Column(db.Text)
    password = db.Column(db.String(225))